# 사용자에게 하나를 선택받는다. ['가위', '바위', '보']
user_choice = input(" 가위, 바위, 보 중 하나를 선택하세요: ")

# random 모듈 (무작위 관련 함수를 포함)
import random

# 컴퓨터의 선택지를 리스트로 정의 
choices = ['가위','바위','보']

# 랜덤 함수를 만든다.
computer_choice = random.choice(choices)

# 컴퓨터의 선택 출력
print(f"컴퓨터의 선택:{computer_choice}")

# 결과 출력 (인덱스 0,1,2)
if user_choice in choices:
    # 사용자와 컴퓨터의 선택을 choices 리스트에서의 인덱스로 변환
    user_choice_index = choices.index(user_choice)
    computer_choice_index = choices.index(computer_choice)
    
    # 결과가 무승부
    if user_choice_index == computer_choice_index:
        print("결과: 무승부입니다!")
    # 사용자 승
    elif (user_choice_index == 0 and computer_choice_index == 1) or \
        (user_choice_index == 1 and computer_choice_index == 2) or \
        (user_choice_index == 2 and computer_choice_index == 0):
        print("결과: 당신이 졌습니다!")
    # 컴퓨터 승
    elif (computer_choice_index == 0 and user_choice_index == 1) or \
        (computer_choice_index == 1 and user_choice_index == 2) or \
        (computer_choice_index == 2 and user_choice_index == 0):
        print("결과: 당신이 이겼습니다!")
    # 입력 오류
    else:
        print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")


