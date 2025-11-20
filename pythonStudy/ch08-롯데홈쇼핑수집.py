import time
from selenium import webdriver
from selenium.webdriver.common.by import By

keyword = input("상품 입력 >> ")
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)
browser.get(f"https://www.lotteimall.com/search/searchMain.lotte?slog=00101_1&headerQuery={keyword}")
time.sleep(3)
name = browser.find_elements(By.CSS_SELECTOR, "p.title > a")
for i in name:
    print(i.text)
browser.close()