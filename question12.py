# 사용자로부터 초기값(baseValue)을 입력받아 전역 변수로 선언

baseValue = float(input("기본값을 입력하세요: "))

# selectOperation()함수 정의
# 전역변수 사용하여 각각의 연산 코드 작성
# 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 선택지를 만든다.

def selectOperation():
    
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")

    Numberinput = int(input("선택:"))
    selectNumber = float(input("숫자 입력: "))
    
    if Numberinput == 1:
        return (f"연산 결과: {baseValue + selectNumber} ")
    elif Numberinput == 2:
        return (f"연산 결과: {baseValue - selectNumber}")
    elif Numberinput == 3:
        return (f"연산 결과: {baseValue * selectNumber}")       
    elif Numberinput == 4:
        if selectNumber == 0:
            return  ("에러: 0으로 나눌 수 없습니다.")
        else :
             return  (f"연산 결과: {baseValue / selectNumber}") 
        
        
result = selectOperation()
print(result)