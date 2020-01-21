from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import os

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def get_images(base_url, url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    image_links = [each.get('src') for each in images]
    links = []
    for each in image_links:
        if base_url in each:
            links.append(each)
    return links

print('Enter type of Images separated by space!!!!')
types = input().split(' ')
os.mkdir('folder')
for type_ in types:
    images = get_images('https://images.unsplash.com/photo','https://unsplash.com/s/photos/{}'.format(type_))
    with open('folder/{}.txt'.format(type_), "w") as file:
        for img in images:
            file.write('{}'.format(img))
            file.write('\n')
    file.close()