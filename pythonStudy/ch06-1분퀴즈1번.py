import requests
from bs4 import BeautifulSoup

code = requests.get("https://www.moviechart.co.kr/rank/realtime/index/image") # "로 감싸기
soup = BeautifulSoup(code.text, "html.parser") # .text 붙이기
title = soup.select("h3 > a") # >>를 >로 수정
for i in title:
    print(i.text) # title을 i로 수정