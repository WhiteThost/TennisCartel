import requests
from bs4 import BeautifulSoup


URL = "https://www.betway.pt/desportos/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="live-table")



#games = soup.find_all("div", class_="container__fsbody")
print('eeeeeeee')
print(soup)