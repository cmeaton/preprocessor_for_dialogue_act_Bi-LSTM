# preprocessor_for_dialogue_act_Bi-LSTM


### Overview
This repo contains the necessary code to preprocess data from the [Switchboard Dialogue Act Corpus](https://github.com/cgpotts/swda) so that it can be fed into the included dialogue act prediction model. 

### Model
The model used is from the paper ['Dialogue Act Sequence Labeling using Hierarchical encoder with CRF'](https://arxiv.org/pdf/1709.04250.pdf). I am not the author of the model. Source code from the model was written by the author of this  [repo](https://github.com/YanWenqiang/HBLSTM-CRF). I am not the author of the model source code. I have made a few edits to the original code, such as writing/importing some helper functions and modifying hyperparameters to reflect those published in the paper. See *HBLSTM-CRF.py*.

### Preprocessing scripts
The source code did not include a script to preprocess SWBD data so that it could be fed into the model. To solve this problem, I wrote two scripts, *swbd_utterance_parser.py* and *swbd_preprocessor.py*.

**swbd_utterance_parser.py:** This code inputs the raw transcript files from the SWBD corpus, cleans text data, numerically categorizes DA labels, and saves a clean csv file for each transcript, named by transcript id. This has already been run and the parsed data can be found in '/swda_paresed'. To run this code, download the SWBD corpus from the link above. Depending on how many transcripts you would like to process at once, see lines 12 and 14. Call with:

$ python swbd_utterance_parser.py .

**swbd_preprocessor.py:** This code inputs clean transcripts (output from swbd_utterance_parser.py). The entire corpus is deconstructed (flattened) to create a BOW numerical representation for each word (int). The integers are then reconstructed into the hierarchical format required by the model, example below:

[] = corpus

[[]] = transcript

[[[]]] = utterance

*example_data* = [[['my feet are cold'],[why dont you put on slippers],[good idea],[[why did the scarecrow get a blue ribbon],[why],[because he was outstanding in his field]]]

Example data is converted into BOW representation:

*bow_example_data* = [[[1,2,3,4],[5,6,7,8,9,10],[11,12]],[[13,14,15,16,17,18,19,20],[13],[21,22,23,24,25,26,27]]]

Dialogue act labels for each utterance are converted into numerical categories (1-42) and returned in the following shape:

*example_labels* = [[1,2,1],[2,2,1]]

This script relies on a class from *swda.py*, which I am also not the author of. I included it in this repo, but it can also be downloaded from the SWBD repo above. 

**Instead of calling swbd_preprocessor.py and saving preprocessed data**, the necassary functions are integrated into the actual model code. Simply run HBLSTM-CRF.py to preprocess the parsed SWBD data and feed it directly into the model for training. Call with:

$ python HBLSTM-CRF.py

### Dependencies:
- Python 3
- Tensorflow 1.14.0
- Sci-kit learn
- Pandas
- Numpy

### Notes:
  - 10/07/2019: The model runs properly on the first 4 transcripts. Aside from this, any combination of transcripts in the data set (regardless of specific transcript files, training size, and batchSize). Have not been able to solve this issue.
  - **GOAL:** Train the model using 70% for training, 20% for development, and 10% for testing.





