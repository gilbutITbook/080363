import requests
from bs4 import BeautifulSoup
import urllib.request as req

code = requests.get("https://www.sisul.or.kr/open_content/skydome/introduce/pop_subway.jsp")
soup = BeautifulSoup(code.text, "html.parser")
image_element = soup.select_one("div.center > img")
img_url = "https://www.sisul.or.kr" + image_element.attrs["src"]
req.urlretrieve(img_url, "지하철 노선도.png")