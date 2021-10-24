import pandas as pd

import re
import neologdn

def main():
    df = pd.read_csv('titles.csv')

    treated_titles = []
    for title in df['titles']:
        new_title = re.sub(r'【.+】', '', title)
        new_title = neologdn.normalize(new_title)
        treated_titles.append(new_title)

    df['treated_titles'] = treated_titles

    df.to_csv('datasets.csv', index=False)

if __name__=='__main__':
    main()