import pandas as pd

import re
import neologdn

def main():
    df = pd.read_csv('titles.csv')

    treated_titles = []
    for title in df['titles']:
        new_title = re.sub(r'【.+】', '', title)
        # new_title = neologdn.normalize(new_title)
        # 終了トークンを追加
        new_title = new_title + '<|endoftext|>'
        treated_titles.append(new_title)

    dataset = "\n".join(treated_titles)

    with open('dataset.txt', 'w') as f:
        f.write(dataset)

if __name__=='__main__':
    main()