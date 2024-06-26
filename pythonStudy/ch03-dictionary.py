price = {"짜장면": 6000, "짬뽕": 7000, "탕수육": 20000}
print(price["짜장면"]) # price 딕셔너리의 특정 원소 출력
price["짬뽕밥"] = 7500 # price 딕셔너리에 새 원소 추가
del(price["짬뽕"]) # price 딕셔너리의 특정 원소 삭제
price["짜장면"] = 6500 # price 딕셔너리의 특정 원솟값 수정
print(price)

fruit = {"사과": 2000, "포도": 3500, "오렌지": 4500}
result = fruit.items() # fruit 딕셔너리의 모든 키-값을 쌍으로 가져오기
print(list(result)) # 딕셔너리를 리스트형으로 변환해 출력

school = {
    "1반": [
        {"이름": "김민수", "성적": {"수학": 90, "과학": 88, "영어": 94}},
        {"이름": "박서연", "성적": {"수학": 82, "과학": 95, "영어": 88}}
    ],
    "2반": [
        {"이름": "이지훈", "성적": {"수학": 61, "과학": 95, "영어": 56}},
        {"이름": "최윤아", "성적": {"수학": 89, "과학": 83, "영어": 100}}
    ],
    "3반": [
        {"이름": "정하윤", "성적": {"수학": 77, "과학": 87, "영어": 95}},
        {"이름": "송태민", "성적": {"수학": 84, "과학": 96, "영어": 46}}
    ]
}
print(school["1반"][0]["성적"]["수학"]) # 1반 김민수 학생의 수학 성적 출력
print(school["3반"][1]["성적"]["영어"]) # 3반 송태민 학생의 영어 성적 출력