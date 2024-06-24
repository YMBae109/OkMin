integer = int(input("첫 번째 숫자(정수)를 입력하세요: "))
float_num = float(input("두 번째 숫자(부동 소수점 수)를 입력하세요: "))

total = integer + float_num # 묵시적 형변환 (Implicit type conversion)
print(type(integer))
if total <= 100:
    print("합이 100 이하입니다: ",total) 
else :
    print("합이 100을 초과합니다:",total)
    print(type(integer))
    