# 함수 정의
# 출석 점수 - 주당 수업시간, 결석 시간, 지각 횟수
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    total_hours = hours_per_week * 15
    absent = int(tardy_count / 3 + absence_hours)
    attendance_score = 20 - (20 * absent / total_hours) 
    
    if attendance_score >  total_hours / 4 :
        print("당신의 출석 점수는 F (학점 미부여)점입니다.")
        
    else :
        print(f"당신의 출석 점수는 {attendance_score:.2f}점입니다.")
# 사용자 입력

hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

# 함수를 호출하고 출력
attendance_score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)