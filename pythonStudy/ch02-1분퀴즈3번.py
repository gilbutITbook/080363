height = int(input("키 입력 (cm) >> "))
weight = int(input("몸무게 입력 (kg) >> "))
bmi = round(weight/(height/100)**2, 2) # round() 함수: 숫자 반올림
print("당신의 BMI(체질량지수)는", bmi, "입니다.")