# # 체크 함수 선언
# def reservation_check(age, event_code, reservation_date):
#     success = "예약이 완료되었습니다!"
    
#     # 잘못된 입력
#     if event_code not in ("E1","E2","E3") or not 1 <= reservation_date <= 30:
#         return "잘못된 입력입니다. 프로그램을 종료합니다."

#     # 사용자의 이벤트 코드
#     if event_code == "E1":
#         if age >= 18 :
#             return success
#         else : 
#             return "나이 제한으로 인해 예약할 수 없습니다."
#     elif event_code == "E2":
#         if reservation_date % 2 == 0:
#             return success
#         else :
#             return "선택하신 날짜에는 예약할 수 없습니다."
#     elif event_code == "E3":
#         # E3 코드 만 16세 이상
#         if age >= 16 and reservation_date % 7 == 0 :
#             return success
#         elif age < 16:
#             return "나이 제한으로 인해 예약할 수 없습니다."
#         else :
#             return "선택하신 날짜에는 예약할 수 없습니다."
            
# # 입력

# age = int(input("나이를 입력하세요: "))
# event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
# reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# # 변수 선언

# reservation_system = (reservation_check(age, event_code, reservation_date))

# # 결과 값 출력

# print(reservation_system)


# 2차-------------------------------------------------------------------------------

# 함수 정의 
'''def reservation_system(age, event_code, reservation_date):
    
    
    msg = ("예약이 완료되었습니다!")
    msg_age = ("나이 제한으로 인해 예약할 수 없습니다.")
    msg_date = ("선택하신 날짜에는 예약할 수 없습니다.")
    
    # 잘못된 입력 먼저 작성
    if event_code not in ["E1","E2","E3"] or 1 > reservation_date or reservation_date > 30:
        return ("잘못된 입력입니다. 프로그램을 종료합니다.")
    
    else :
        # E1 코드 작성
        if event_code == "E1":
            if age >= 18 :
                return msg
            else :
                return msg_age
        # E2 코드 작성        
        elif event_code == "E2":
            if reservation_date % 2 == 0 :
                return msg
            else :
                return msg_date
                
        # E3 커드 작성
        elif event_code == "E3":
            if age >= 16 and reservation_date % 7 == 0 :
                return msg_
            else :
                if age < 16:
                    return msg_age
                else :
                    return msg_date
      
# 사용자에게 입력받기 

age = int(input("나이를 입력하세요: "))
event_code = str(input("예약하려는 이벤트 코드를 입력하세요: "))
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 출력

total = reservation_system(age, event_code, reservation_date)

print(total)'''


# 함수 정의

def reservation_system(age, event_code, reservation_date):
    # 이벤트 코드 리스트 생성
    event_code = ['E1','E2','E3']
    # 메세지 
    suc_msg = "예약이 완료 되었습니다."
    error_msg = "잘못된 입력입니다. 프로그램을 종료합니다." 
    age_msg = "나이 제한으로 인해 예약할 수 없습니다."
    date_msg = "선택하신 날짜에는 예약할 수 없습니다."
    
    # E1
    if event == event_code[0]:
        if age >= 18:
            return suc_msg
        else :
            return age_msg
        
    # E2
    elif event == event_code[1]:
        if reservation_date % 2 == 0:
            return suc_msg
        else:
            return date_msg
        
    # E3 
    elif event == event_code[2]:
        if age >= 16 and age % 7 == 0:
            return suc_msg
        else :
            return error_msg
        
    else :
        return error_msg
    
age = int(input())
event = input()
reservation_date = int(input())

result = reservation_system(age, event, reservation_date)

print(result)
        