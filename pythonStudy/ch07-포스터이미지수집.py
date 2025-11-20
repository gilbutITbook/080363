import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os

code = requests.get("https://www.moviechart.co.kr/rank/realtime/index/image")
soup = BeautifulSoup(code.text, "html.parser")
title_elements = soup.select("h3 > a")
image_elements = soup.select("li.movieBox-item > a > img")

# 이미지 내려받을 폴더 생성
folder_name = "./무비차트 포스터"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

num = 1
for title, image in zip(title_elements, image_elements):
    print(f"제목 : {title.text}")
    img_url = "https://www.moviechart.co.kr" + image.attrs["src"]
    req.urlretrieve(img_url, f"{folder_name}/{num}.jpg")
    num += 1
    print("----------------------------")