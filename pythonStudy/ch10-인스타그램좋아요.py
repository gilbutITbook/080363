from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 크롬 브라우저 열어 인스타그램 로그인 페이지 접속
keyword = input("해시태그 입력 >> ")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

# 로그인
id = browser.find_element(By.NAME, "username")
id.send_keys("여기에 인스타그램 아이디 입력")
pw = browser.find_element(By.NAME, "password")
pw.send_keys("여기에 인스타그램 비밀번호 입력")
button = browser.find_element(By.CSS_SELECTOR, "form#loginForm > div > div:nth-child(3)")
button.click()
time.sleep(7)

# 해시태그 검색 페이지 접속
browser.get(f"https://www.instagram.com/explore/search/keyword/?q=%23{keyword}")
time.sleep(6)

# 첫 번째 게시물 클릭
first_photo = browser.find_element(By.CSS_SELECTOR, "div._aagu")
first_photo.click()
time.sleep(5)

# 좋아요 자동 누르기 시작
while True:
    like = browser.find_element(By.CSS_SELECTOR, "section.x78zum5.x1q0g3np.xwib8y2.x1yrsyyn.x1xp8e9x.x13fuv20.x178xt8z.xdj266r.x14z9mp.xat24cr.x1lziwak.xo1ph6p.xv54qhq.xf7dkkf span > svg")
    next = browser.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh > button._abl- svg")
    # like 요소의 aria-label 속성값이 "좋아요"이면
    if like.get_attribute("aria-label") == "좋아요":
        browser.execute_script("document.querySelector('svg[aria-label=\"좋아요\"]').dispatchEvent(new MouseEvent('click', {bubbles: true}));")
        time.sleep(2)
        next.click()
        time.sleep(2)
    # like 요소의 aria-label 속성값이 "좋아요 취소"이면
    else:
        next.click()
        time.sleep(2)