from bs4 import BeautifulSoup
import requests
#add f_string to autogenerate the url
source = requests.get('https://manybooks.net/search-book?field_genre[30]=30')
content = source.content

soup = BeautifulSoup(content, 'lxml')
item_list = []
div = soup.find_all('article', class_='book')
for link in div:
    a_tag = link.find('a')
    img = link.find('img', class_='img-responsive')
    crude = []
    if a_tag is not None:
        for shit in a_tag:
             crude.append(a_tag.attrs['href'])
             crude.append(img.attrs['src'])
             crude.append(img.attrs['alt'])
        item_list.append(crude)
    else:
        print('None Mfucker')

print(item_list[3][2])
