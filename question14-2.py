'''
# 사용자 입력 받기
numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")

# 문자열을 숫자 리스트로 변환
numbers = numbers_str.split(',')

total = 0
list = []
for num in numbers:
    total += int(num)
    list += num
if total < 100:
    print(f"입력된 모든 숫자들: {list}\n최종 총합: {total}")
elif to
    print(f"총합이 100을 초과하였습니다.\n현재까지의 입력값들: {list}\n현재까지의 총합: {total}") '''
    
    

input_num_list = input("숫자를 입력하세요 : ")

num_list = input_num_list.split(",")

sum = 0
output_list = []

for num_str in num_list:
    num = int(num_str)
    sum += num
    output_list.append(num)
     
    if sum > 100:
        over_100_flag = True
        break
    
if over_100_flag:
    print("100 초과", sum)
    print(output_list) 
else:
    print("100 이하", sum)
    print(output_list)



# 숫자를 문자열로 입력 input()

number_str = input("숫자들을 쉼표로 구분하여 입력하세요")

# 개별 숫자로 분리

number = number_str.split(',')

# 정수 변환 후 모든 숫자의 합을 계산
total = 0
output_list = []

for num_str in number:
    num = int(num_str)
    total += num
    output_list.append(num)
    # 총합이 100초과 하면 그 순간 총합 출력하고 종료
    if total > 100:
        print("총합이 100을 초과하였습니다.")
        print(f"현재까지의 입력값들: {output_list}")
        print(f"현재까지의 총합: {total}")
        break
    # 100초과하지 않는 경우 최종 총합과 입력된 숫자들을 출력 
else:
    print("총합이 100을 초과하지 않았습니다.")
    print("입력된 모든 숫자들: ",output_list)
    print("최종 총합", total)




    