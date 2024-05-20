num = 1
while num <= 3:
    print("Hello World")
    num += 1

while True:
    foo = input("문자열 입력 >> ")
    if foo == "종료":
        break
    elif foo == "":
        print("아무것도 입력하지 않았습니다. 다시 입력해주세요.")
        continue
    print(f"현재 입력된 글자의 수는 {len(foo)}개입니다.")