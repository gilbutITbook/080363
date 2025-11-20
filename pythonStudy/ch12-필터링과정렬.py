import pandas as pd

df = pd.read_excel("./엑셀데이터/아파트분양가.xlsx")
result = df[(df["지역명"] == "서울") | (df["지역명"] == "부산")]
result = result.sort_values(by="분양가", ascending=False)
print(result.to_string())