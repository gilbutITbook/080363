import requests
from bs4 import BeautifulSoup
code = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
soup = BeautifulSoup(code.text, "html.parser")
title = soup.select("strong.title")
for i in title:
    print(i.text)