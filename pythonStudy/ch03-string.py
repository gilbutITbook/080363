print("강아지가 '멍멍' 짖는다")
print('강아지가 "멍멍" 짖는다')
print("""그는
안녕이라고
인사한다""")
print('''그는
"""안녕"""이라고
인사한다''')
print("난\n파이썬이\n좋아") # 행갈이
print("난\t파이썬이\t좋아") # 탭 기능
print("I\tLOVE\tPYTHON") # 탭 기능
print("난\\파이썬이\\좋아") # 문자열 내 역슬래시를 그대로 출력
print("난\"파이썬이\"좋아") # 문자열 내 큰따옴표를 그대로 출력
print('난\'파이썬이\'좋아') # 문자열 내 작은따옴표를 그대로 출력
print('난 파이썬이 좋아\b\b') # 백 스페이스 기능
print('난 파이썬이 좋아\rHello World') # 커서를 문장 처음으로 이동
string1 = "10"
string2 = "20"
print(string1 + string2) # 문자열끼리의 덧셈
print(string1 * 10) # 문자열과 숫자의 곱셈
foo = "Hello World"
print("Hello" in foo) # Hello World 문자열에 Hello라는 글자가 있는가
print("abcd" in foo) # Hello World 문자열에 abcd라는 글자가 있는가
print("Hello" not in foo) # Hello World 문자열에 Hello라는 글자가 없는가
print("abcd" not in foo) # Hello World 문자열에 abcd라는 글자가 없는가
string = "Hello_World_Hello_Python"
result = string.split("_") # _를 기준으로 문자열 나누기
print(result)
foo = input("문자열 입력 >> ")
print("현재 입력된 글자의 수는 {len(foo)}개입니다.")
