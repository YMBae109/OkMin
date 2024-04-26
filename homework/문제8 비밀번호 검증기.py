# 사용자로부터 비밀번호 입력
password = input("비밀번호를 입력하세요: ")

# 비밀번호 3가지 기준 작성
# 문자열 길이 확인
if len(password) >= 8:
    
    # 숫자가 포함되어 있는지 확인
    has_number = False
    for char in password:
        if char.isdigit(): 
            has_number = True
            break
            
        # 대문자가 포함되어 있는지 확인
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break 

    if has_number and has_uppercase:
        print("비밀번호가 안전합니다.")
    else :
        print("비밀번호가 안전하지 않습니다.")
else :
    print("비밀번호가 안전하지 않습니다.")     
    
    
     
            