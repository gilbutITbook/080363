import requests
from bs4 import BeautifulSoup

code = requests.get(f"http://underkg.co.kr/news")
soup = BeautifulSoup(code.text, "html.parser")
title = soup.select("h1.title > a")
for i in title:
    print(f"제목 : {i.text}")
    news_url = i.attrs['href']
    print(f"링크 : {news_url}")
    code_news = requests.get(news_url)
    soup_news = BeautifulSoup(code_news.text, "html.parser")
    content = soup_news.select_one("div.read_body")
    print(content.text.replace("\n", "").strip())
    print("--------------------------------------")