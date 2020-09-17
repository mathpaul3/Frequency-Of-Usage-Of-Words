import requests
from bs4 import BeautifulSoup
import os
from Postposition import Crawling

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.foxnews.com/politics')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
news_URLs = soup.select(
    '#wrapper > div > div.page-content > div > main > section.collection.collection-article-list.has-load-more > div '
    '> article > div.info > header > h4 > a')


politics_URL = {}

for title in news_URLs:
    politics_URL[title.text] = title.get('href')

for (key, value) in politics_URL.items():
    if value.find('video.foxnews.com') == -1:
        print('https://www.foxnews.com' + value)
        Crawling.crawl('https://www.foxnews.com' + value)
