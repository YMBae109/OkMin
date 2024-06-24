
# 항상 요구사항에 맞게 프로그램을 작성한다

# 알고리즘을 정리 한 후 코딩을 실시
# 단위 별 작성
# 예외처리를 빼놓고 기능만 구현해도 B이상

line = '-' * 20
menu = (f"{line}\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n{line}")

# 메뉴 출력
while True:
    
    print(menu)
    input_num = int(input("원하는 메뉴 번호를 입력하세요: "))

    # 입력 값 함수 설정
    def multiply_input():
        # 사용자로부터 출력할 구구단의 범위를 입력 받음
        input_user = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n").split("~") 
        
        # list를 해제하여 저장
        multiply(*input_user)
        
    # 출력 값 함수 설정
    def multiply(arg_1, arg_2 = False):
        # 받은 값을 정수로 변환
        arg_1, arg_2 = int(arg_1), int(arg_2)
        
        # if 2 ~ 9사이의 값 입력 시 구구단 계산
        # 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
        if (1 < arg_1 < 10) and arg_2 == False:
            for num in range(1,10):
                print (f"{arg_1} * {num} = {arg_1 * num}")
        
        # arg_2 값이 있으면 범위 구구단 출력  
        elif (1 < arg_1 < 10) and (1 < arg_2 < 10):        
            for j in range(arg_1, arg_2 + 1):
                print()
                for num in range(1, 10):
                    print(f"{j} * {num} = {j * num}")  
        
        # 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
        else:
            print("2~9 사이의 값을 입력하세요")
            multiply_input()
        
    # 구구단 출력 1
    if input_num == 1:
        multiply_input() 
        

    # 랜덤값 삼각형 출력 2        
    elif input_num == 2:
        import random
        
        # 사용자로부터 삼각형의 높이 2 or 3줄 입력 받음
        while True:
            input_height = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하): "))

            # 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
            if input_height == 2:
                three_list = []
                for _ in range(3):
                    three_list.append(random.randint(0,9))
                print(" ",three_list[0])
                print(three_list[1],three_list[2])
            
            elif input_height == 3:
                three_list = []
                for _ in range(9):
                    three_list.append(random.randint(0,9))
                print(" ",three_list[0])
                print(three_list[1],three_list[2])
                 
            # 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
            else :
                print("2 또는 3을 입력하세요")

    # 종료 3
    # 프로그램을 종료
    elif input_num == 3:
        print("프로그램을 종료합니다.")
        break
    
    # 예외 처리
    else :
        print("1~3 사이 정수를 입력하세요")