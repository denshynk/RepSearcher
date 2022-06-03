import requests
from bs4 import BeautifulSoup as BS
import os

page = 1

while True:
    url = "https://github.com/orgs/HowProgrammingWorks/repositories?page=" + str(page)
    r = requests.get(url)
    soup = BS(r.content, 'html.parser')
    teme = soup.find_all('h3', class_="wb-break-all")


    if(len(teme)):
        for temes in teme:
            temes = temes.find("a", {'class':'d-inline-block'})
            if temes is not None:
                print(temes.text)
        page += 1
    else:
        break

