# 합계와 평균을 계산하기 위한 변수 값 초기 설정
total = 0

# 사용자로부터 5개의 정수 입력받기
for i in range(5):
    number = int(input(f"{1+i}번째 값 입력"))
    
    # 입력받은 수를 총합에 더하기
    total += number

# 출력
print(f"합계 :{total}")
print(f"평균 :{total/5:.1f}")
