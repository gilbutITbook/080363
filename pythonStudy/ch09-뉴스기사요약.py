import json
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from gtts import gTTS
from playsound import playsound

code = requests.get("https://www.joongang.co.kr/money")
soup = BeautifulSoup(code.text, "html.parser")
title_list = soup.select("ul.card_right_list.rank_list h2.headline > a")
# 기사 제목 띄우기
print(" [ 중앙일보 경제 뉴스 ] ")
for index, title in enumerate(title_list):
    print(f"{index + 1} - {title.text.strip()}")
print("----------------------------------------------------")
# 수집할 기사 선택
user_choice = int(input("확인할 뉴스를 선택하세요 >> "))
# 선택한 기사의 본문 링크 가져오기
user_item = title_list[user_choice - 1]
news_title = user_item.text
news_link = user_item.attrs["href"]
# newspaper 모듈로 기사 본문 가공 및 출력
article = Article(news_link, language='ko')
article.download()
article.parse()
news_content = article.text
print(news_content)
# news_content의 글자 수를 1900자로 자르기
if len(news_content) >= 1900:
    news_content = news_content[:1900]
client_id = "여기에 Cliend id 넣기"
client_secret = "여기에 client secret 넣기"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}
data = {
    "document": {
        "title": news_title,
        "content": news_content
    },
    "option": {
        "language": "ko",
        "model": "news",
        "tone": 3,
        "summaryCount": 6
    }
}
url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
response = requests.post(url, data=json.dumps(data), headers=headers)
response_dict = json.loads(response.text)
print("---------------------------------------------")
print("[문서 요약 결과]")
print(response_dict["summary"])
comment_to_voice = gTTS(text=response_dict["summary"], lang="ko")
comment_to_voice.save("news.mp3")
playsound("news.mp3")