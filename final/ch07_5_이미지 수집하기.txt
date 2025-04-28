import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os

code = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
soup = BeautifulSoup(code.text, "html.parser")
title_elements = soup.select("strong.title")
image_elements = soup.select("span.thumb-image > img")

# 이미지 내려받을 폴더 생성
folder_name = "./CGV 무비차트 포스터"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
num = 1
for title, image in zip(title_elements, image_elements):
    print(f"제목 : {title.text}")
    img_url = image.attrs["src"]
    req.urlretrieve(img_url, f"{folder_name}/{num}.jpg")
    num += 1
    print("----------------------------")