# BoolQ
This project attempts to solve the BoolQ task from the SuperGLUE benchmark using various approaches

## Approach3

This approach is an extension to Approach1 and Approach2 wherein, along with the pre-trained models and entailment we try to integrate entity linking and relation extraction to gather some useful information that could help answer the question more accurately.

This approach has a number of methods and modules:


### MainApplication: BoolQ.ipynb

This method uses 5 different pre-trained models and compares their performance on the BoolQ task.

To run the models follow the below instructions:

1) Clone this repo on a local machine
2) Go to Google Colab https://colab.research.google.com/notebooks/intro.ipynb#recent=true and upload the notebook ./Approach3/BoolQ.ipynb

#### Evaluating the models on data augmented with entity description of entities present in both question and passage. (Contributor: Dhawal)

If you plan to run this work, please follow the instruction below:

3) Upload the dataset files from the ./Approach3/AugmentedData_Dhawal on Colab.
4) Run each cell one by one.
5) At the last cell(Testing) enter a choice of model or select all models to perform the BoolQ task. You'll be asked to enter a few different hyperparamters, if not sure, enter the values given as examples in the prompt.
6) The last cell also gives an option to load saved models for evaluation. The models can be downloaded from the link below: 
https://unh.box.com/v/augDhawalSavedModels
7) Once downloaded, unzip the models to ./models/augDhawal directory.

If you plan to run the techniques by Bhavya use the following instructions:
3) Upload the dataset files from the ./Approach3/Augmented_data_Bhavya on Colab.
4) Run each cell one by one.
5) As there are no saved models for Bhavya's techniques...please use the option Fine-tune and Evaluate.
6) At the last cell(Testing) enter a choice of model or select all models to perform the BoolQ task. You'll be asked to enter a few different hyperparamters, if not sure, enter the values given as examples in the prompt.




