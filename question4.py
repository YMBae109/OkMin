# # 변수 선언

# def calculate_averge(math_score, science_score, english_score):
#     return(math_score + science_score + english_score) / 3

# # 사용자에게 수학,과학,영어 점수를 각각 입력받는다.

# math_score = float(input("수학 점수를 입력하세요: "))
# science_score = float(input("과학 점수를 입력하세요: "))
# english_score = float(input("영어 점수를 입력하세요: "))

# averge = calculate_averge(math_score, science_score, english_score)

# # 평균 점수에 따른 학점 등급을 계산하는 코드 작성하고 출력

# if averge >= 90:
#     print(f"평균 점수는{averge:.1f}이고 학점은 A입니다.")
# elif 80 <= averge < 90:
#     print(f"평균 점수는{averge:.1f}이고 학점은 B입니다.")
# elif 70 <= averge < 80:
#     print(f"평균 점수는{averge:.1f}이고 학점은 C입니다.")
# elif 60 <= averge < 70:
#     print(f"평균 점수는{averge:.1f}이고 학점은 D입니다.")
# elif averge < 60:
#     print(f"평균 점수는{averge:.1f}이고 학점은 F입니다.")
    
# 2회 -------------------------------------------------------------

# 세 과목의 평균점수를 계산 하는 함수 정의
def average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3

    # 각 등급에 맞는 결과 리턴
    if average >= 90 :
        return (f"평균 점수는 {average:.1f}점이고, 학점은 A입니다.")
    elif 80 <= average :
        return (f"평균 점수는 {average:.1f}점이고, 학점은 B입니다.")
    elif 70 <= average :
        return (f"평균 점수는 {average:.1f}점이고, 학점은 C입니다.")
    elif 60 <= average :
        return (f"평균 점수는 {average:.1f}점이고, 학점은 D입니다.")
    else : 
        return (f"평균 점수는 {average:.1f}점이고, 학점은 F입니다.")
    
# 사용자에게 입력받기

math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

average_score = average(math_score, science_score, english_score)

# 함수 호출

print(average_score)