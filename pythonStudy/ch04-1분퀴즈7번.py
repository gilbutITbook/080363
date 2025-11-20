data = {"사과": 5, "바나나": 7}
try:
    print(data["오렌지"])
except KeyError:
    print("그 과일은 딕셔너리에 없습니다.")
except:
    print("알 수 없는 오류입니다.")