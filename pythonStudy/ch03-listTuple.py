fruit = ["사과", "포도", "오렌지", "바나나"]
print(["사과", "포도", "오렌지", "바나나"][0])
print(fruit[2])
print(fruit[-1])
print(fruit[-4])

print(fruit[1:3]) # 1, 2번 원소 추출
print(fruit[0:3]) # 0, 1, 2번 원소 추출
print(fruit[:3]) # 0, 1, 2번 원소 추출
print(fruit[2:4]) # 2, 3번 원소 추출
print(fruit[2:]) # 2, 3번 원소 추출

fruit1 = ["사과", "포도", "오렌지"]
fruit2 = ["수박", "귤", "바나나"]
print(fruit1 + fruit2) # fruit1와 fruit2 연결
print(fruit1 * 3) # fruit1을 세 번 연결
print("포도" in fruit1) # fruit1 리스트 중에 "포도"라는 원소가 있는지 확인
print("자몽" not in fruit1) # fruit1 리스트 중에 "자몽"이라는 원소가 없는지 확인
print("포도@" in fruit1) # fruit1 리스트 중에 "포도@"라는 원소가 있는지 확인

fruit.append("자몽") # 원소 추가(리스트 맨 마지막에 추가)
print(fruit)
fruit.remove("바나나") # 원소 삭제(원소의 값을 이용해 삭제)
print(fruit)
del(fruit[2]) # 원소 삭제(원소의 인덱스를 이용해 삭제)
print(fruit)
fruit[0] = "수박" # 원소 수정
print(fruit)

foo = ["영희", "철수", "민희", "상혁"]
result = foo.index("상혁")
print(result)

foo1 = ("a", "b", "c") # 튜플 foo1 선언
foo2 = ("d", "e", "f") # 튜플 foo2 선언
print(foo1[0]) # foo1 튜플의 0번 원소 출력
print(foo1[:2]) # foo1 튜플의 0, 1번 원소 출력
print(foo1 + foo2) # foo1, foo2 튜플 연결
print(foo1 * 2) # foo1 튜플 두 번 연결
print(len(foo1)) # foo1 튜플의 원소 수 출력
foo1.append("d") # foo1 튜플에 원소 추가 시도
foo1.remove("b") # foo1 튜플에 원소 삭제 시도
foo1[0] = "A" # foo1 튜플의 원솟값 수정 시도