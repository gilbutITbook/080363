import requests
from bs4 import BeautifulSoup

keyword = input("키워드 입력 >> ")
code = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}")
soup = BeautifulSoup(code.text, "html.parser")
title = soup.select("div.related_srch div.tit")
for i in title:
    print(i.text)