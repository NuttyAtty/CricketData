import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import numpy as np

def extract_stats(url):
    page = get(url).text
    bs = BeautifulSoup(page, 'lxml')

    nos = bs.findAll('table', {'class':'engineTable'})

    table = nos[2]

    headers = []
    titles = table.findAll('th')
    for item in titles:
        headers.append(item.text)

    body = table.findAll('tr')
    headings = body[0]
    tablebody = body[1:]
    rows = []

    for row_num in range(len(tablebody)):
        row = []
        for row_item in tablebody[row_num].findAll('td'):
            aa = row_item.text
            row.append(aa)


        rows.append(row)

    df = pd.DataFrame(data=rows, columns=headers)
    df.to_csv('output_statsguru.csv', index=False)

def main():
    url = ''
    print('Enter/Paste ESPNCricinfo Statsguru url:')
    url = input()
    extract_stats(url)




if __name__ == '__main__':
    main()

