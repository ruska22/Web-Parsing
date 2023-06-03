import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
file = open('notes.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['title,' 'artist', 'price'])
for ind in range(1, 6):
    url = 'https://www.sheetmusicdirect.com/Search.aspx?query=Piano&page=' + str(ind)
    r = requests.get(url)
    # print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.find('tbody')
    notes = body.find_all('tr')
    for note in notes:
        songtitle = note.find('span', class_='songtitle')
        note_title = songtitle.a.text.strip()
        artist = note.find('td', class_='song-artist')
        artist_name = artist.text.strip()
        pr = note.find('td', class_='price')
        price = pr.text.strip()
        print(price)
        file_obj.writerow([note_title, artist_name, price])
    sleep(randint(15, 20))
file.close()