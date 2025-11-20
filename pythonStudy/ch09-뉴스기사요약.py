import requests
from bs4 import BeautifulSoup
from newspaper import Article
from groq import Groq
from gtts import gTTS
from playsound import playsound

code = requests.get("https://www.joongang.co.kr/money")
soup = BeautifulSoup(code.text, "html.parser")
title_list = soup.select("ul.card_right_list.rank_list h2.headline > a")

# 기사 제목 띄우기
print(" [ 중앙일보 경제 뉴스 ] ")
for index, title in enumerate(title_list):
    print(f"{index+1} - {title.text.strip()}")
print("----------------------------------------------------")

# 수집할 기사 선택
user_choice = int(input("확인할 뉴스를 선택하세요 >> "))

# 선택한 기사의 본문 링크 가져오기
user_item = title_list[user_choice-1]
news_title= user_item.text
news_link = user_item.attrs["href"]

# newspaper 모듈로 기사 본문 가공 및 출력
article = Article(news_link, language='ko')
article.download()
article.parse()
news_content = article.text
print(news_content)

# Groq API 호출 및 응답받기
client = Groq(
    api_key="발급받은_API_key_입력"
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"다음 뉴스 본문을 한국어로 3줄로 간략히 요약해줘. 각 요약 항목은 줄바꿈해. {news_content}"
        }
    ],
    model="llama-3.3-70b-versatile",
)

# 기사 요약문 출력
print("-------------------------------------------")
print("[기사 요약 결과]")
print(chat_completion.choices[0].message.content)

# 텍스트-음성 변환
comment_to_voice = gTTS(text=chat_completion.choices[0].message.content, lang="ko")
comment_to_voice.save("news.mp3")
playsound("news.mp3")