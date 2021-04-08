# BoolQ
This project attempts to solve the BoolQ task from the SuperGLUE benchmark using various approaches

## Approach1

In this approach we attempt to solve the BoolQ task using pre-trained language models like BERT, RoBERTa, etc along with soem custom neural network models and also try to use textual entailment as a move to improve the performance.

This approach has three methods divided into three different files:

### Method1: BoolQ.ipynb

This method uses 5 different pre-trained models and compares their performance on the BoolQ task.

To run the models follow the below instructions:

1) Clone this repo on a local machine
2) Go to Google Colab https://colab.research.google.com/notebooks/intro.ipynb#recent=true and upload the notebook ./Approach1/BoolQ.ipynb
3) Upload the dataset files from the ./Dataset directory on Colab.
4) Run each cell one by one.
5) At the last cell(Testing) enter a choice of model or select all models to perform the BoolQ task. You'll be asked to enter a few different hyperparamters, if not sure enter the values given as examples in the prompt.

NOTE: The results are printed out on the screen during training and evaluation along with plots of the training loss and accuracy.
The accuracy and F1-score for a given model is also written to a file named as resultsMODEL_NAME.txt (e.g. resultsBERT.txt).

### Method2: EntailmentEnsemble.ipynb

Data Set Required:
1) MultiNLI Dataset : See the train_data.csv and val_data.csv
2) Bool Q Dataset : Common Across all submissions (included in EntailmentEnsemble.ipynb)

Instruction Set:
1) Clone the repo on a local machine
2) Go to Google Colab https://colab.research.google.com/notebooks/intro.ipynb#recent=true and upload the notebook EntailmentEnsemble.ipynb
3) Load the files train_data.csv and val_data.csv
4) Run each cell one by one.
5) Across the notebook Graphs are plotted and results are printed.

### Method3: Submission1.ipynb

1) Go to Google Colab https://colab.research.google.com/notebooks/intro.ipynb#recent=true and upload the notebook Submission1.ipynb.
2) Run each cell one by one.
3) No need to load dataset files as data is being downloaded directly in collab sheet.

## Approach2

This approach is an extension to Approach1 wherein, along with the pre-trained models and entailment we try to integrate entity linking to gather some useful information that could help answer the question more accurately.

This approach has a number of methods and modules:

### EntityLinking

This directory contains the code used to perform entity linking. We applied two entity linking modules Spacy and REL and compared the results of the two.
The output of each entity linker is present in the respective directories.

### Method1: BoolQ.ipynb

This method uses 5 different pre-trained models and compares their performance on the BoolQ task.

To run the models follow the below instructions:

1) Clone this repo on a local machine
2) Go to Google Colab https://colab.research.google.com/notebooks/intro.ipynb#recent=true and upload the notebook ./Approach2/BoolQ.ipynb
3) Upload the dataset files from the ./Dataset and ./Approach2/Entity_Dataset directory on Colab.
4) Run each cell one by one.
5) At the last cell(Testing) enter a choice of model or select all models to perform the BoolQ task. You'll be asked to enter a few different hyperparamters, if not sure, enter the values given as examples in the prompt.

NOTE: The results are printed out on the screen during training and evaluation along with plots of the training loss and accuracy.
The accuracy and F1-score for a given model is also written to a file named as resultsMODEL_NAME.txt (e.g. resultsBERT.txt).







