contents = input("문장 입력 >> ") # 변수명은 달라도 됨
result = contents.replace('제주도', '#제주도').replace('여행', '#여행').replace('맛집', '#맛집') # replace() 함수 적용 순서는 상관없음
print(f"결과: {result}")