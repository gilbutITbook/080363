import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.get("https://cafe.daum.net/talingpython/rRa6")
time.sleep(1)

# 파일이 존재하지 않으면 자동으로 파일 생성
if not os.path.exists("./중고나라.txt"):
    open("./중고나라.txt", "w")

while True:
    # 과거에 크롤링한 제목 불러오기
    with open("./중고나라.txt", "r", encoding="utf-8") as f:
        crawled_title = f.read().split("\n")
    browser.switch_to.frame("down")
    # 중고나라 게시글 제목 크롤링
    title = browser.find_elements(By.CSS_SELECTOR, "a.txt_item")
    new_one = 0
    for i in title:
        if i.text not in crawled_title:  # 새 게시글 제목이면
            print(f"[알림] 새로운 글이 올라왔어요! - {i.text}")
            with open("./중고나라.txt", "a", encoding="utf-8") as f:
                f.write(i.text + "\n")  # 새 게시글 제목을 txt 파일에 기록
                # 새 게시글 제목에 관심 물건 명칭이 포함된 경우
                if "청소기" in i.text:
                    new_one += 1
    # 관심 물건이 1개 이상일 때만 메시지 출력
    if new_one >= 1:
        print(f"[알림] 청소기 관련 글이 {new_one}개 올라왔습니다.")
        tag = "pythonstudy_1234"
        headers = {"Title": "중고나라 관심 물건 알림"}
        message = f"[알림] 청소기 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6"
        headers["Title"] = headers["Title"].encode("utf-8")
        requests.post(f"https://ntfy.sh/{tag}", data=message.encode("utf-8"), headers=headers)
    browser.refresh()  # 새로 고침
    time.sleep(10)