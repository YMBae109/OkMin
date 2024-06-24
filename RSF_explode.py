# 초기값 설정

# 인간 
win = 0
draw = 0
lose = 0

# 컴퓨터 리스트 생성

computer = ["가위", "바위", "보"]

# while 문 작성으로 2선승제 까지 무한루프

    # 사용자가 가위 바위 보 중 하나 입력
import random

while True :
    N = input("가위, 바위, 보 중 하나를 입력하세요: ")
    ai = random.choice(computer)
    print(f"컴퓨터: {ai}")
    if win == 2 or lose == 2 :
        break
    
    elif N == "가위":
        if ai == "가위":
            draw += 1 
        elif ai == "바위":
            lose += 1
        elif ai == "보":
            win += 1

########################################################################

import random

# 가위, 바위, 보 게임 만들기
# 다중 대입
count_win, count_lose, count_draw = 0, 0, 0


while True: # 언제 브레이크 (초!,중,말)
    # 승리 횟수가 2번 이상 또는 패배 횟수가 2번 이상이면, 프로그램 종료
    if count_win == 2 or count_lose == 2:
        print("승리 : ", "사용자" if count_win == 2 else "컴퓨터")
        
        break
        
    # 사용자로부터 입력 받기
    input_user = input("가위 바위 보 중 입력: ") # 변수명을 맞추면 자동완성이 빠르다

    # 컴퓨터가 랜덤하게 가위, 바위, 보 중 하나를 선택
    # random -> 정수 (integer)
    rsp = ["가위", "바위", "보"]
    input_computer = rsp[random.randint(0, 2)]

    msg_result = ""
    

# 결과 판별
# 1) 무승부 ** 무승부는 같다
    if input_user == input_computer:
        msg_result = "무승부"
        count_draw += 1
        
    # 2) 승 
    elif input_user == "가위" and input_computer == "보" or \
        input_user == "바위" and input_computer == "가위" or \
        input_user == "보" and input_computer == "바위" :
        msg_result = "승"
        count_win += 1
    # 3) 패
    else : 
        msg_result = "패"
        count_lose += 1
    # 출력
    print(f"사용자: {input_user} \t컴퓨터: {input_computer}")
    print(f"전적 : {count_win}승 {count_draw}무 {count_lose}패")
    print(msg_result)