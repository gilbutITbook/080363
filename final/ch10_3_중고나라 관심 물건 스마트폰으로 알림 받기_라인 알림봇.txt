import requests

token = "여기에 복사한 토큰 붙여넣기"
data = {
    "message": "이미지 보내기 테스트 중",
    "imageThumbnail": "https://platum.kr/wp-content/uploads/2020/08/58809805_2597174657088183_7071241453283835904_o.jpg",
    "imageFullsize": "https://platum.kr/wp-content/uploads/2020/08/58809805_2597174657088183_7071241453283835904_o.jpg"
}
requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": f"Bearer {token}"}, data=data)