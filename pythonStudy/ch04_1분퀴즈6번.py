num = int(input("숫자 입력: "))
for i in range(1, num + 1):
    for j in range(i):
        print(i, end=" ")
    print()