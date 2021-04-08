'''This piece of code performs entity linking on the three data files using the REL entity linker'''
# Please follow the installation instructions from https://github.com/informagi/REL/ to install REL
# Also download the required files as mentioned on the installation instructions of REL

from REL.entity_disambiguation import EntityDisambiguation
from REL.mention_detection import MentionDetection
from REL.ner import Cmns, load_flair_ner
from REL.utils import process_results

import pandas as pd
import json
import numpy as np
import json

# Load the data
trainData = pd.read_json("./train.jsonl", lines=True, orient="records")
valData = pd.read_json("./val.jsonl", lines=True, orient="records")
testData = pd.read_json("./test.jsonl", lines=True, orient="records")

# Train 
trainPassages = trainData.passage.values
trainQuestions = trainData.question.values
trainAnswers = trainData.label.values.astype(int)

# Validation
valPassages = valData.passage.values
valQuestions = valData.question.values
valAnswers = valData.label.values.astype(int)

# Test
testPassages = testData.passage.values
testQuestions = testData.question.values


# FinalSet (A combination of all three datasets)
finalPassages = np.concatenate((trainPassages, valPassages))
finalPassages = np.concatenate((finalPassages, testPassages))

finalQuestions = np.concatenate((trainQuestions, valQuestions))
finalQuestions = np.concatenate((finalQuestions, testQuestions))

def example_preprocessing(passage):
    # Example splitting, should be of format {doc_1: {sent_idx: [sentence, []]}, .... }}
    # text = """Obama will visit Germany. And have a meeting with Merkel tomorrow.
    # Obama will visit Germany. And have a meeting with Merkel tomorrow. Go all the way or blah blah Charles Bukowski."""
    spans = []  # [(0, 5), (17, 7), (50, 6)]

    processed = {"test_doc": [passage, spans]}
    return processed


base_url = "C:/Users/dhawa/Documents/CS953/BoolQ/" # This needs to be the address to your project folder
wiki_version = "wiki_2019"  # version of wikipedia you want to use

# Load the mention detection module
mention_detection = MentionDetection(base_url, wiki_version)

# Load the ner taggers
tagger_ner = load_flair_ner("ner-fast")
tagger_ngram = Cmns(base_url, wiki_version, n=5)

# Load the model to perform entity linking.
config = {
    "mode": "eval",
    "model_path": "{}/{}/generated/model".format(base_url, wiki_version),
}

model = EntityDisambiguation(base_url, wiki_version, config)

# File where all the given entities along with their links will be printed to
efile = open("entityLinks.jsonl", 'w')

for passage in finalPassages:
    
    input_text = example_preprocessing(passage)

    mentions_dataset, n_mentions = mention_detection.format_spans(input_text)
    mentions_dataset, n_mentions = mention_detection.find_mentions(input_text, tagger_ner)
    
    # Predict the links
    predictions, timing = model.predict(mentions_dataset)

    result = process_results(mentions_dataset, predictions, input_text)

    # Write the results to the given file
    if result != {}:
        elinks = result['test_doc']
        for e in elinks:
            efile.write(json.dumps({e[2]: e[3]}) + '\n')
