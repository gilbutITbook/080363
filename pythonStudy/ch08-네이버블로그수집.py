import time
from selenium import webdriver
from selenium.webdriver.common.by import By

keyword = input("키워드 입력 >> ")
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)

# 검색 결과 1~5페이지 본문 URL 수집
blog_url_list = []
for page_num in range(1, 6):
    browser.get(f"https://section.blog.naver.com/Search/Post.naver?pageNo={page_num}&rangeType=ALL&orderBy=sim&keyword={keyword}")
    time.sleep(2)
    items = browser.find_elements(By.CSS_SELECTOR, "a.desc_inner")
    for i in items:
        blog_url_list.append(i.get_attribute("href"))

# print(blog_url_list)
# 크롤링 시작
for blog_url in blog_url_list:
    blog_url_for_mobile = blog_url.replace("https://blog.naver","https://m.blog.naver")
    browser.get(blog_url_for_mobile)
    time.sleep(2)
    title = browser.find_element(By.CSS_SELECTOR, "div.se-component-content span")
    content = browser.find_element(By.CSS_SELECTOR, "div.se-main-container")
    print(f"제목 : {title.text}")
    print(content.text.replace("\n", " ").strip())
    print("--------------------------------")
browser.close()