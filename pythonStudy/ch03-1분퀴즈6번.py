shopping_list = input("구매할 물건을 쉼표로 구분해 입력: ")
shopping_list = shopping_list.split(",")
sorted_result = sorted(shopping_list)
print("정렬된 쇼핑 목록:", sorted_result)

# 또는
# print("정렬된 쇼핑 목록:", sorted(input("구매할 물건을 쉼표로 구분해 입력: ").split(",")))