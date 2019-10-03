from swda import Transcript
import glob
import csv
import pandas as pd
import re
import pprint

def parse_utterance_act_tag():
    '''This function iterates through all SWBD transcripts and returns a .csv file containing each individual utterance (str) paired with its DA tag (str) in a list'''
    
    '''If you want to parse all folders'''
    transcripts = glob.glob('swda\*\*')
    '''If you want to parse 1 folder'''
    # transcripts = glob.glob('swda\sw00utt\*')

    
    for i in transcripts:
        trans = Transcript(i, 'swda/swda-metadata.csv')
        num_utt = len(trans.utterances)
        data = []

        for j in range(0,num_utt):
            utt = trans.utterances[j]

            text = utt.text
            tag = utt.damsl_act_tag()
            sex = utt.caller_sex
            da_category = ''

            # convert to lower case
            text = [text.lower()]
            # remove special characters
            text_no_specialchar = re.sub('[^ A-Za-z0-9]+', '', str(text))
        
        # mapping spaff onto DA tags

            if tag == 'sd':
                da_category = '1'
            elif tag == 'b':
                da_category = '2'   
            elif tag == 'sv':
                da_category = '3'
            elif tag == 'aa':
                da_category = '4'
            elif tag == '%':
                da_category = '5'
            elif tag == 'ba':
                da_category = '6'
            elif tag == 'qy':
                da_category = '7' 
            elif tag == 'x':
                da_category = '8' 
            elif tag == 'ny':
                da_category = '9'
            elif tag == 'fc':
               da_category = '10'
            elif tag == '%':
                da_category = '11' 
            elif tag == 'qw':
                da_category = '12'
            elif tag == 'nn':
                da_category = '13'
            elif tag == 'bk':
                da_category = '14'
            elif tag == 'h':
               da_category = '15'
            elif tag == 'qy^d':
                da_category = '16' 
            elif tag == 'fo_o_fw_by_bc':
                da_category = '17'
            elif tag == 'bh':
                da_category = '18'
            elif tag == '^q':
                da_category = '19'
            elif tag == 'bf':
                da_category = '20'
            elif tag == 'na':
                da_category = '21'
            elif tag == 'ad':
                da_category = '22'
            elif tag == '^2':
               da_category = '23'
            elif tag == 'b^m':
                da_category = '24' 
            elif tag == 'qo':
                da_category = '25'
            elif tag == 'qh':
                da_category = '26'
            elif tag == '^h':
                da_category = '27'
            elif tag == 'ar':
                da_category = '28'
            elif tag == 'ng':
                da_category = '29'
            elif tag == 'br':
                da_category = '30'
            elif tag == 'no':
               da_category = '31'
            elif tag == 'fp':
               da_category = '32'
            elif tag == 'qrr':
               da_category = '33'
            elif tag == 'arp_nd':
                da_category = '34'
            elif tag == 't3':
                da_category = '35'
            elif tag == 'oo_co_cc':
                da_category = '36'
            elif tag == 't1':
               da_category = '37'
            elif tag == 'bd':
               da_category = '38'
            elif tag == 'aap_am':
               da_category = '39'
            elif tag == '^g':
               da_category = '40'
            elif tag == 'qw^d':
                da_category = '41'
            elif tag == 'fa':
               da_category = '42'
            elif tag == 'ft':
                da_category = '43'
            else:
                da_category = '0'
            
            data.append([text, text_no_specialchar, tag, sex, da_category])
            pprint.pprint(data)
            print(f'{i} is finished'.format(i=i))
    
            df = pd.DataFrame(data, columns = ['utterance','utterance_no_specialchar', 'da_tag', 'speaker_sex', 'da_category'])
            try:
                df.to_csv(f'swda_parsed\\{i[13:-8]}.csv'.format(i=i), index=False)
            except:
                pass

parse_utterance_act_tag()
