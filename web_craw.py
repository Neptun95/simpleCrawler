import requests
import csv
from bs4 import BeautifulSoup


def craw():
    url = "https://www.youtube.com/watch?v=3dXbmAl3LSY"

    response = requests.get(url=url)

    html = BeautifulSoup(response.text, 'html.parser')

    autor = html.find_all('span', 'author')

    bewertungen = html.find_all('section class', 'reviewBody')


    autoren = list()
    for a in autor:
        autoren.append(a)
    
    bewertungList = list()
    for b in bewertungen:
        bewertungList.append(b)
    
    lisDic = []
    for t in zip(autoren, bewertungen):
        lisDic.append(t)
        
    return lisDic
    
if __name__ == '__main__':
    text = craw()
    print(text)
