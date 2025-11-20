for word in ["사과", "포도", "오렌지"]:
    print(word)

menu = ["짜장면", "짬뽕", "탕수육"]
price = [6000, 7000, 20000]
for a, b in zip(menu, price):
    print(f"{a}은 {b}원입니다.")

name_list = ["철수", "영희", "영수", "옥순"]
for i, name in enumerate(name_list):
    print(f"{i+1}등: {name}")
