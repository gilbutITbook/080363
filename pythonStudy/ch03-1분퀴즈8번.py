# 현재 환율 정보
exchange_rates = {
"USD": 1200, # 1달러가 1200원
"EUR": 1400, # 1유로가 1400원
"JPY": 11 # 1엔이 11원
}
print("--------- 환율 정보 추가/수정 ---------")
key = input("추가하거나 수정할 통화를 입력하세요: ")
value = int(input(f"{key}의 현재 환율 금액을 입력하세요: "))
exchange_rates[key] = value
print("--------- 환율 계산기 ---------")
currency = input(f"통화({list(exchange_rates.keys())})를 입력하세요: ")
price = int(input(f"변환할 금액({currency})을 입력하세요: "))
print(f"환율 계산 결과: {exchange_rates[currency] * price}원")