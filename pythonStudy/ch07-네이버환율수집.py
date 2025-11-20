import requests
from bs4 import BeautifulSoup

code = requests.get("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code.text, "html.parser")
price = soup.select("ul#exchangeList span.value")
for i in price:
    print(i.text)