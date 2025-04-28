from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)
browser.get("https://www.youtube.com/watch?v=_-ugbwhhApI")
time.sleep(3)
prev_height = 0
same_num_cnt = 0

while True:
    ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
    cur_height = browser.execute_script("return document.documentElement.scrollTop")
    if prev_height == cur_height:
        same_num_cnt += 1
    else:
        same_num_cnt = 0
    if same_num_cnt == 200:
        break
    prev_height = cur_height

comments = browser.find_elements(By.CSS_SELECTOR, "#content-text")
for i in comments:
    print(i.text.replace("\n", "").strip())

browser.close()