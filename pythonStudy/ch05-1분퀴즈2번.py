# 함수 정의
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return a / b
    else:
        return "지원하지 않는 연산자입니다."

# 함수 호출
print(calculator(10, 5, '+')) # 출력: 15
print(calculator(10, 5, '-')) # 출력: 5
print(calculator(10, 5, '*')) # 출력: 50
print(calculator(10, 5, '/')) # 출력: 2.0
print(calculator(10, 0, '/')) # 출력: 0으로 나눌 수 없습니다.
print(calculator(10, 0, '@')) # 출력: 지원하지 않는 연산자입니다.