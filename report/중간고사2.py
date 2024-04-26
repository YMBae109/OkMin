# 프로그램 선택 
select_menu = input("---------------------------\n1. 홀수 짝수 구분 프로그램\n2. 3의 배수 확인 프로그램\n---------------------------\n메뉴를 선택해 주십시오.\n")

# 1.홀수 짝수 구분 프로그램 작성

if select_menu == "1":
    print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
    # 정수 입력
    inputValue = int(input("정수 값을 입력하세요.\n"))
    # 홀수 -> 입력값 % 2 != 0 짝수 -> 입력값 % 2 == 0
    if inputValue % 2 != 0:
        print(f"입력하신 값 {inputValue} 홀수 입니다.")
    else :
        print(f"입력하신 값 {inputValue} 짝수 입니다.")
    
# 2. 3의 배수 확인 프로그램 작성

elif select_menu == "2":
    print("3의 배수 확인 프로그램을 선택 하셨습니다.")
    # 정수 입력
    inputValue = int(input("정수 값을 입력하세요.\n"))
    # 3의 배수 -> 입력값 % 3 == 0 
    if inputValue % 3 == 0:
        print(f"입력하신 값 {inputValue}, 3의 배수입니다.")
    else :
        print(f"입력하신 값 {inputValue}, 3의 배수가 아닙니다.")
    
# 1,2외 잘못된 메뉴 값 선택시 오류메세지 출력

else :
    print(f"입력하신 값 {select_menu}은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다.")
