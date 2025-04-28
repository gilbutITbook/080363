import openpyxl
import pandas as pd
from pandas import ExcelWriter

writer = ExcelWriter("./엑셀데이터/장사시설_병합.xlsx")

for year in range(2021, 2025):
    # 장례식장 시설정보 시트를 읽어와 데이터프레임으로 변환
    df = pd.read_excel(f"./엑셀데이터/장사시설현황/{year}년/전국장사시설현황.xlsx", sheet_name="장례식장 시설정보")
    # df에서 시설명, 주소, 전화번호만 추출해 df_data에 저장
    df_data = df[["시설명", "주소", "전화번호"]]
    # print(df_data.to_string())
    df_data.to_excel(writer, sheet_name=f"{year}년")
    print(f"{year}년 데이터 병합 완료")

writer.close()

book = openpyxl.load_workbook("./엑셀데이터/장사시설_병합.xlsx")

for year in range(2021, 2025):
    sheet = book[f"{year}년"]
    sheet.column_dimensions["B"].width = 37
    sheet.column_dimensions["C"].width = 70
    sheet.column_dimensions["D"].width = 14

book.save("./엑셀데이터/장사시설_병합.xlsx")