import json
import pandas as pd
import re


def map_strings_using_csv(S):
    
    mapping_dict = dict(zip(df_map['from'], df_map['to']))

    for key, value in mapping_dict.items():
        S = S.replace(key, value)
    S = S.replace('°', ' degree ')
    S = S.replace('**', '??')
    S = re.sub(r'\s+', ' ', S)
    S = re.sub(r'\\uline{ }', '', S.strip())
    S = re.sub(r'-+', '-', S.strip())

    if S.startswith('('):
        S = re.sub(r'\([^)]*\)', '', S, 1)

    return S


if __name__ == '__main__':

    # Read the CSV file into a Pandas DataFrame
    df_map = pd.read_csv('char map.csv')

    question_df = pd.read_json('TAL-SAQ6K-EN.jsonl', lines=True)

    for i in range(len(question_df)):
        ques = question_df['problem'].iloc[i]
        ques = map_strings_using_csv(ques)
        if str(r'~\uline{~~~~~~~~~~}~') in ques:
            ques = ques.replace(r'~\uline{~~~~~~~~~~}~', '  ')
            # question_df['problem'].iloc[i] = ques
        if str(r'\overset') in ques:
            ques = ques.replace(r'\overset{ }', '  ')
            # print(sub_ques)

        question_df['problem'].iloc[i] = ques

    question_df.to_json('TAL-SAQ6K-EN_mod.jsonl', orient='records', lines=True)
