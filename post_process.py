import json
import pandas as pd
from datetime import datetime
import argparse
import re


def convert_to_float_latex(latex_string):
    # LaTeX string representing the fraction
    pattern = r'-?\\frac{(\d+)}{(\d+)}'
    match = re.match(pattern, latex_string)

    if match:
        try:
            numerator = int(match.group(1))
            denominator = int(match.group(2))
            if latex_string.startswith('-'):
                return - numerator / denominator
            else:
                return numerator / denominator
        except:
            return latex_string
    else:
        return latex_string

def convert_to_float(frac_str):
    if type(frac_str) is list:
        frac_str = frac_str[0]

    if '/' not in frac_str:
        return convert_to_float_latex(frac_str)
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
            try:
                leading, num = num.split(' ')
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
        except:
            return frac_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--answer", default="test_tora_5927_seed42_t0.0_s0_e5927_01-12_16-29.jsonl", type=str)
    args = parser.parse_args()
    
    result_df = pd.read_json(args.answer, lines=True)
    result_df['pred'] = result_df['pred'].apply(convert_to_float)
    submission = pd.Series(result_df.pred.values,index=result_df.queId).to_dict()

    # save to json file
    with open(f'TAL_SAQ6K_EN_prediction.json', "w") as outfile:
        json.dump(submission, outfile)
