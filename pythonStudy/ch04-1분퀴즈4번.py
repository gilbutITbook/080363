username = "user"
password = "pass123"
attempt_count = 0
while attempt_count < 3:
    input_username = input("사용자명을 입력하세요: ")
    input_password = input("비밀번호를 입력하세요: ")
    if input_username == username and input_password == password:
        print("로그인 성공!")
        break
    else:
        print("로그인 실패. 다시 시도해주세요.")
        attempt_count += 1
    if attempt_count == 3:
        print("로그인 시도 횟수를 초과했습니다.")