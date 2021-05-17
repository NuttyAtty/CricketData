import csv
import pandas as pd  # file operations
from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq # For requesting data from link
import numpy as np
import re

def main():
    url = "howstat1.html"
    with open(url) as fp:
        bs = BeautifulSoup(fp, 'html5lib')


    table = bs.find("table", {"class": "TableLined"})

    with open('AZ.csv', 'a', newline='') as csvfile:
        f = csv.writer(csvfile)

        for x in table:
            rows = table.find_all('tr')
            for tr in rows:
                data = []
                cols = tr.find_all('td')
                for td in cols:
                    data.append(td.text.strip())
                f.writerow(data)
                print(data)







if __name__ == '__main__':
    main()