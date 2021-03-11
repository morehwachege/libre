from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.betika.com/lite/?ck=1')

content = source.content

soup = BeautifulSoup(content, 'lxml')

urls = []
div = soup.find_all('div', class_='game highlights--item')
for link in div:
    a_tag = link.find('a')
    name = link.find('div', class_='teams-info-vert-left')
    if a_tag is not None:
        urls.append(a_tag.attrs['href'])
        urls.append(name.text)

for url in urls:
    print(url)
