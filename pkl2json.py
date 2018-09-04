import json
import pickle


with open('table_2018_09_02_13_23.pkl', 'br') as pkl:
    with open('tw0102.json', 'wt') as trs:

        json.dump(
            pickle.load(pkl), trs,
            ensure_ascii=False, sort_keys=True, indent=2,
        )
