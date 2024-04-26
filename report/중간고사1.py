# 입력받은 문자열을 적절한 숫자 형식으로 변환하는 함수
# 문자열에 소수점이 포함되어 있으면 실수(float)으로,
# 그렇지 않으면 정수(int)로 변환하여 반환한다. 
def safe_convert(value):
    if '.' in value:
        return float(value)
    else :
        return int(value)
    
# 첫 번째 값을 입력 받는다.
inputValue_str = input("첫 번째 값을 입력하세요: ")
# 입력받은 값을 함수를 호출하여 적절한 숫자 형식으로 반환
inputValue = safe_convert(inputValue_str)

# 두 번째 값을 입력 받는다
inputValue2_str = input("두 번째 값을 입력하세요: ")
# 입력받은 값을 함수를 호출하여 적절한 숫자 형식으로 반환
inputValue2 = safe_convert(inputValue2_str)

# 연산자 (+, -, *, /) 중 하나를 입력받는다
operator = input("연산자를 선택하세요(+, -, *, / 중 하나 입력)")

# 선택한 연산자에 따른 if 문을 각각 작성 
if operator == '+':
    resultValue = inputValue + inputValue2
elif operator == '-':
    resultValue = inputValue - inputValue2
elif operator == '*':
    resultValue = inputValue * inputValue2
elif operator == '/':
    resultValue = inputValue / inputValue2
    
# 결과 값 자료형(interger, float, string) 중 하나를 입력받는다
data_type = input("결과 값 자료형(integer, float, string 중 하나 입력)")

# 자료형에 따른 if 문을 각각 작성
if data_type == "integer":
    resultValue = int(resultValue)
elif data_type == "float":
    resultValue = float(resultValue)
elif data_type == "string":
    resultValue = str(resultValue)

# 결과 값을 출력한다
# 연산자에 따라 식을 다르게 출력한다
print(f"{inputValue_str} {operator} {inputValue2_str} = {resultValue}")