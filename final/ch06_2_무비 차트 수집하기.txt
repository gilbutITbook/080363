import requests
from bs4 import BeautifulSoup

# 서버로부터 HTML 코드 받아오기
code = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
# print(code.text)
# HTML 코드 정리하기
soup = BeautifulSoup(code.text, "html.parser")
# print(soup)
# 원하는 요소 가져오기
# title = soup.select_one("strong.title")
# print(title.text)
# 여러 요소 한 번에 가져오기
title = soup.select("strong.title")
num = 1
for i in title:
    print(f"{num}위 : {i.text}")
    num += 1