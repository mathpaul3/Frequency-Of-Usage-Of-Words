import requests
from bs4 import BeautifulSoup
import json
import os
from Postposition import ReadingFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def crawl(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    news_titles = soup.select(
        '#wrapper > div.page-content > div.row.full > main > article > header > h1'
    )
    news_articles = soup.select(
        '#wrapper > div.page-content > div.row.full > main > article > div > div > div.article-body > p'
    )

    politics_title = {}
    politics_article = {}

    for title in news_titles:
        politics_title[title.text] = title.get('h1')

    with open(os.path.join(BASE_DIR, 'politics_title.json'), 'a') as json_file:
        json.dump(politics_title, json_file)

    for article in news_articles:
        politics_article[article.text] = article.get('p')

    with open(os.path.join(BASE_DIR, 'politics_article.json'), 'a') as json_file:
        json.dump(politics_article, json_file)

    ReadingFile.function('title')
    ReadingFile.function('article')
