import platform
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

# 복사 붙여넣기 함수
def copy_and_paste(browser, css, user_input):
    pyperclip.copy(user_input)
    browser.find_element(By.CSS_SELECTOR, css).click()
    os_type = platform.system()
    if os_type == "Windows":
        paste_key = Keys.CONTROL
    else:
        paste_key = Keys.COMMAND
    ActionChains(browser).key_down(paste_key).key_down("V").perform()

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(1)

# 로그인하기
copy_and_paste(browser, "input#id", "여기에 아이디 입력")
time.sleep(1)
copy_and_paste(browser, "input#pw", "여기에 비밀번호 입력")
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, "button.btn_login").click()
time.sleep(2)