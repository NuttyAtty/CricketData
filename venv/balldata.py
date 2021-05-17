import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

def extract_ball_data(filename):

    with open(filename) as fp:
        bs = BeautifulSoup(fp, 'html5lib')

    ball_data = pd.DataFrame(columns=['ball','bowler_batsman','result','commentary','length', 'line'])



    ball_numbers = list()
    bowler_batsman = list()
    result = list()
    commentary = list()

    for div in bs.find_all('span', {'class': 'match-comment-over'}):
        ball_numbers.append(div.text)



    for div in bs.find_all('div', {'class': 'match-comment-short-text'}):
        bowler_batsman.append(div.text)



    for div in bs.find_all('div', {'class': 'match-comment-run'}):
        result.append(div.text)



    for div in bs.find_all('div', itemprop='articleBody'):
        commentary.append(div.text)

    ballnos = pd.Series(ball_numbers)
    bowlbat = pd.Series(bowler_batsman)
    res = pd.Series(result)
    comm = pd.Series(commentary)





    ball_data.ball = ballnos
    ball_data.bowler_batsman = bowlbat
    ball_data.result = res
    ball_data.commentary = comm




    fil1 = ['yorker', 'block hole', 'full toss', 'fulltoss', 'full-toss', 'Yorker', 'Block hole', 'Full toss', 'Fulltoss', 'Full-toss']
    fil2 = ['full', 'fullish', 'tossed up', 'full length', 'fuller', 'under his nose', 'Full', 'Fullish', 'Tossed up', 'Full length', 'Fuller', 'Under his nose']
    fil3 = ['length', 'good length', 'length ball', 'goodish', 'back of a length', 'flat', 'length delivery', 'flatter', 'cover', 'covers', 'mid-on', 'long-on', 'midon', 'longon', 'Length', 'Good length', 'Length ball', 'Goodish', 'Back of a length', 'Flat', 'Length delivery', 'Flatter', 'Cover', 'Covers', 'Mid-on', 'Long-on', 'Midon', 'Longon']
    fil4 = ['short', 'shortish', 'bouncer', 'short length', 'chin music', 'pull', 'pulls', 'pulled', 'hook', 'hooks', 'hooked', 'ducks', 'ducked', 'Short', 'Shortish', 'Bouncer', 'Short length', 'Chin music', 'Pull', 'Pulls', 'Pulled', 'Hook', 'Hooks', 'Hooked', 'Ducks', 'Ducked']
    fil5 = ['outside off', 'corridor', 'wider', 'reaches out', 'slip', 'slips', 'slip catch', 'cover', 'covers', 'point', 'gully', 'wide', 'wider', 'Outside off', 'Corridor', 'Wider', 'Reaches out', 'Slip', 'Slips', 'Slip catch', 'Cover', 'Covers', 'Point', 'Gully', 'Wide', 'Wider']
    fil6 = ['off', 'off stump', 'off side', 'off drive', 'Off', 'Off stump', 'Off side', 'Off drive']
    fil7 = ['middle', 'middle stump', 'middle and leg', 'Middle', 'Middle stump', 'Middle and leg']
    fil8 = ['leg stump', 'leg side', 'leg', 'legs', 'pads', 'pad', 'fine', 'Leg stump', 'Leg side', 'Leg', 'Legs', 'Pads', 'Pad', 'Fine']
    length = list()
    line = list()




    for element in commentary:
        if any(x in element for x in fil1):
            length.append('Yorker')
        elif any(x in element for x in fil2):
            length.append('Full')
        elif any(x in element for x in fil3):
            length.append('Good')
        elif any(x in element for x in fil4):
            length.append('Short')
        else:
            length.append('Unknown')

    for element in commentary:
        if any(x in element for x in fil5):
            line.append('Outside Off')
        elif any(x in element for x in fil6):
            line.append('Off Stump')
        elif any(x in element for x in fil7):
            line.append('Middle Stump')
        elif any(x in element for x in fil8):
            line.append('Leg Stump')
        else:
            line.append('Unknown')

    len = pd.Series(length)
    lin = pd.Series(line)



    ball_data.length = len
    ball_data.line = lin

    print(ball_data)
    csv = ''
    print('Enter CSV/Excel filename:')
    csv = input()
    ball_data.to_csv(csv +'.csv', index=False)

def main():
    filename = ''
    print('Enter saved ESPN Cricinfo commentary HTML page directory(with forward slashes):')
    filename = input()
    extract_ball_data(filename)





if __name__ == '__main__':
    main()
