import requests

tag = "pythonstudy_1234"
headers = {"Title" : "제목 테스트"}
message = "테스트 중입니다."
headers["Title"] = headers["Title"].encode("utf-8")
headers["Attach"] = "https://platum.kr/wp-content/uploads/2020/08/58809805_2597174657088183_7071241453283835904_o.jpg"
requests.post(f"https://ntfy.sh/{tag}", data=message.encode("utf-8"), headers=headers)