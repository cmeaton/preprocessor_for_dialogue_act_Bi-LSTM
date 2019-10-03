import pandas as pd
import glob
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


path = glob.glob(r'C:\Users\conno\code\nlp\swda\swda_parsed\*.csv')

def read_data(path):
    '''This function reads in a list of file paths, creates a dataframe from each path,
    and appends each df to a dictionary.'''

    df_dict = {}
    for i in path:
        df = pd.read_csv(str(i))
        df = df.dropna()
        df_dict[i] = pd.read_csv(i)

    return df_dict

def strucutre_words(df_dictionary):
    '''This function reads in a dictionary of dataframes of transcripts and returns the words of the 
    transcript into the proper format for feeing into the model.'''
    
    raw_utt_list = []

    for name,df in df_dictionary.items():
        utt = df.utterance_no_specialchar.to_list()
        raw_utt_list.append(utt)
        
    processed_utt_list = [] 
    for i in raw_utt_list:
        utt_split_words = []
        for j in i:
            utt_split_words.append((j.split()))
        processed_utt_list.append(utt_split_words) 
    
    return processed_utt_list

def structure_labels(df_dictionary):
    '''This function reads in a dictionary of dataframes of transcripts and returns the utterance DA labels of the 
    transcript into the proper format for feeing into the model.'''
    
    raw_label_list = []

    for name,df in df_dictionary.items():
        lab = df.da_category.to_list()
        raw_label_list.append(lab) 

    processed_label_list = [] 
    for i in raw_label_list:
        label_ = []
        for j in i:
            label_.append((j))
        processed_label_list.append(label_)
        
    return processed_label_list

def flatten(data):  
    '''Input data and flatten list to create transcript-wide BOW'''

    flat_list = [item for sublist in data for item in sublist]
    flat_list = [item for sublist in flat_list for item in sublist]
    values = [word for line in flat_list for word in line.split()]
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    labels = list(integer_encoded)
    mapping = {word: label for word, label in zip(values, labels)}
   
    return mapping, values, labels

def replace(words_with_structure, flat_labels):
    """
    Recursively go through lst and replace every `word`
    with the word and its mapping: (`word`: mapping[`word`])
    """
    
    labels_iter = iter(flat_labels)
    words_and_labels = []

    for convo in words_with_structure:
        words_and_labels.append([])
        for sent in convo:
            words_and_labels[-1].append([])
            word_length = len(sent)
            count = 0
            while count != word_length:
                for word in sent[count].split(' '):
                    words_and_labels[-1][-1].append([word,(next(labels_iter))])
                    count += 1
                
    text = list() 
    ints = list() 
    for i in words_and_labels: 
        text_inner = list() 
        ints_inner = list() 
        for e in i:  
            t, n = zip(*e) 
            text_inner.append(list(t)) 
            ints_inner.append(list(n)) 
        text.append(text_inner) 
        ints.append(ints_inner) 

    return ints


words = strucutre_words(read_data(path))
labels = structure_labels(read_data(path))
mapping, val, lab = flatten(words)
structred_labels = replace(words,lab)

