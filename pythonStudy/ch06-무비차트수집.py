import requests
from bs4 import BeautifulSoup

# 서버로부터 HTML 코드 받아오기
code = requests.get("https://www.moviechart.co.kr/rank/realtime/index/image")
# print(code.text)

# HTML 코드 정리하기
soup = BeautifulSoup(code.text, "html.parser")
# print(soup)

# 원하는 요소 가져오기
# title = soup.select_one("h3 > a")
# print(title.text)

# 여러 요소 한 번에 가져오기
title = soup.select("h3 > a")
num = 1
for i in title:
    print(f"{num}위 : {i.text}")
    num += 1