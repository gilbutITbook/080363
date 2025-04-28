from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login")

# 로그인
id = browser.find_element(By.CSS_SELECTOR, "input#loginId--1")
id.send_keys("여기에 다음 아이디 입력")
pw = browser.find_element(By.CSS_SELECTOR, "input#password--2")
pw.send_keys("여기에 다음 비밀번호 입력")
button = browser.find_element(By.CSS_SELECTOR, "button.btn_g.highlight.submit")
button.click()
# '로봇이 아닙니다'가 나올 경우 다음 코드 추가
# input("로봇이 아닙니다.를 직접 해결한 후 엔터를 쳐주세요 >> ")
# button.click()
time.sleep(3)

# 카페 들어가기
browser.get("http://cafe.daum.net/talingpython")
time.sleep(2)
browser.switch_to.frame("down") # 프레임 전환

# 가입 인사 게시판 클릭
browser.find_element(By.CSS_SELECTOR, "#fldlink_lF1R_309").click()
time.sleep(2)

# 첫 게시물 클릭
browser.find_element(By.CSS_SELECTOR, "a.txt_item").click()
time.sleep(1)

# 댓글 달기
browser.find_element(By.CSS_SELECTOR, "div.box_textarea > textarea").send_keys("반갑습니다 :) ")
time.sleep(1)

# 등록 버튼 클릭
browser.find_element(By.CSS_SELECTOR, "button.btn_g.full_type1.confirm_button").click()

# 다시 뒤로 가기
browser.back()
time.sleep(1)
browser.switch_to.frame("down") # 프레임 전환

# 카페 글쓰기 버튼 클릭
browser.find_element(By.CSS_SELECTOR, "#article-write-btn").click()
time.sleep(2)

# 제목 작성
browser.find_element(By.CSS_SELECTOR, "input.title__input").send_keys("가입 인사 드립니다!")
browser.switch_to.frame("keditorContainer_ifr") # 프레임 전환

# 본문 작성
browser.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("파이썬 공부하러 왔어요. 잘 부탁드립니다~!")
browser.switch_to.default_content() # 최상위 프레임으로 변경
browser.switch_to.frame("down") # 프레임 전환

# 등록 버튼 클릭
browser.find_element(By.CSS_SELECTOR, "button.btn_g.full_type1").click()
time.sleep(2)
browser.close()