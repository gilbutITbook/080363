while True:
    try:
        x = int(input("숫자 입력 >> "))
        result = 10 / x
    except ZeroDivisionError:
        print("0으로는 어떠한 값도 나누지 못합니다! 다시 입력하세요.")
        continue
    except ValueError:
        print("문자는 입력하지 못합니다! 다시 입력하세요.")
        continue
    except:
        print("알 수 없는 오류입니다. 다시 입력하세요.")
        continue
    print(result)