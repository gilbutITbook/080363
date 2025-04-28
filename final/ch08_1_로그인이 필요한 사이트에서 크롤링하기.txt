import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)
browser.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Fmail.daum.net#login")

# 로그인하기
id = browser.find_element(By.CSS_SELECTOR, "input#loginId--1")
id.send_keys("여기에 아이디 입력")
pw = browser.find_element(By.CSS_SELECTOR, "input#password--2")
pw.send_keys("여기에 비밀번호 입력")
button = browser.find_element(By.CSS_SELECTOR,"button.btn_g.highlight.submit")
button.click()

time.sleep(2) # 로그인이 완료될 때까지 2초 기다리기

# 이메일 제목 수집
title = browser.find_elements(By.CSS_SELECTOR, "strong.tit_subject")
for i in title:
    print(i.text)
browser.close()