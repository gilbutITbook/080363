import requests
from bs4 import BeautifulSoup

keyword = input("키워드 입력 >> ")
for page_num in range(1, 11):
    code = requests.get(f"https://kin.naver.com/search/list.naver?query={keyword}&page={page_num}")
    soup = BeautifulSoup(code.text, "html.parser")
    title = soup.select("ul.basic1 a._nclicks\:kin\.txt._searchListTitleAnchor")
    date = soup.select("dd.txt_inline")
    for i, j in zip(title, date):
        print(f"질문 : {i.text}")
        print(f"날짜 : {j.text}")
        print("-------------------------------------------")