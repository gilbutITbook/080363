import mimetypes
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openpyxl

# 첨부파일을 이메일에 넣을 수 있는 형태로 포장하는 함수
def packaging_file(file_name):
    with open(file_name, "rb") as file:
        mimetypes.init()
        mimetype, _ = mimetypes.guess_type(file_name)
        if mimetype is None:
            mimetype = 'application/octet-stream'
        file_type, _, file_subtype = mimetype.partition('/')
        part = MIMEBase(file_type, file_subtype)
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('content-disposition', 'attachment', filename = os.path.basename(file_name))
    return part

naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
naver_id = "여기에 네이버 아이디 입력"
naver_pw = "여기에 네이버 보안설정 비밀번호 입력"
my_mail = f"{naver_id}@naver.com"
naver_server.login(naver_id, naver_pw)
book = openpyxl.load_workbook("./주문내역.xlsx")
sheet = book.active
num = 0
for row in sheet.iter_rows(min_row = 2):
    date = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = f"{name}님, 주문 내역 보내드립니다."
    content = f"""안녕하세요. {name}님. 주문 내역은 다음과 같습니다.
구매일자 : {date}
성함 : {name}
주문제품 : {product}
감사합니다."""
    mail_box = MIMEMultipart()
    mail_box["From"] = my_mail
    mail_box["To"] = your_mail
    mail_box["Subject"] = title
    msg = MIMEText(content, _charset="euc-kr")
    mail_box.attach(msg)
    attached_file = packaging_file("./첨부파일.pdf")
    mail_box.attach(attached_file)
    naver_server.sendmail(my_mail, your_mail, mail_box.as_string())
    print("{}님께 이메일을 보냈습니다.".format(name))
    num += 1
    if num % 20 == 0:
        naver_server.quit()
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
        naver_server.login(naver_id, naver_pw)
