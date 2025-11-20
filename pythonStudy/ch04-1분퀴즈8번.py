numbers = [1, 2, 3]
index = int(input("인덱스를 입력하세요: "))
try:
    print(numbers[index])
except IndexError:
    print("잘못된 인덱스입니다.")