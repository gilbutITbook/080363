import pandas as pd

company_list = ["애플", "아마존", "테슬라"]
df_merge = pd.DataFrame()
for company in company_list:
    df = pd.read_excel(f"./엑셀데이터/2024년_광고비_{company}.xlsx")
    df.set_index("date", inplace=True)
    df_merge[company] = df["total"]
print(df_merge)
df_merge.to_excel("./엑셀데이터/2024년_광고비_병합.xlsx")
