
# text = list(input("주민번호를 입력하세요: "))
# text.remove("-")
# check = [2,3,4,5,6,7,8,9,2,3,4,5] 
# # 주민번호를 한 글자씩 가져와서 234567892345 로 곱한다.
# total = 0
# for character in range(len(check)):
#     total += int(text[character]) * check[character]

# check_num = (11 - (total % 11))  % 10

# # 계산 한 값을 마지막 값과 대응하여 검증하여 출력

# if check_num == int(text[-1]):
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")
    
    
# ##############2회차################################
'''
# 주민번호를 입력받기

resident_number = int(input("주민번호를 입력하세요: ").replace("-",""))

# 체크수의 변수 리스트 선언

check_num = [2,3,4,5,6,7,8,9,2,3,4,5]

# 주민번호와 체크수를 각각 곱하여 덧셈 값을 저장할 변수 선언

total = 0

# 체크 계산

for chararter in check_num:
    total += check_num[i] * resident_number[i]

    last_number = (11-(total / 11)) % 10 
    
# 마지막 자리값이 일치하면 유효한 주민번호, 일치하지 않으면 유효하지 않은 주민번호

if resident_number[-1] == last_number:
    print("유효한 주민번호 입니다.")
else :
    print("유효하지 않은 주민번호입니다.")'''


# ########################################################################
# ###############################교수님 특강 ##############################
# ########################################################################
input_number = "961009-1075115"
check_number = [2,3,4,5,6,7,8,9,2,3,4,5]
print(type(input_number))
# 유효성 검사

sum = 0  # 변수를 선언을 먼저 해주자
count = 0
for num in input_number:
    if num != "-" and count < 12:
        # 현재 num이 "-" 아니고 주민번호의 마지막 자리가 아닐 때
        sum += int(num) * check_number[count]
        count += 1
        

# 주민번호 12자리를 체크 값과 곱한 후 더한다.
# 주민번호 12자리 : 0번째 index -> 11번째 index

 
# 체크값을 계산하다 : (11 - (sum % 11)) % 10
check_value = (11 - (sum % 11)) % 10

# 판별 결과 값을 출력한다.
if check_value == int(input_number[-1]):
    print(type(input_number))
    print("유효한 주민번호")
else:
    print("유효하지 않은 주민번호")
    
######################################################
#######################3회차##########################
######################################################

# # 주민번호 입력
# resident_number = list(input("주민번호를 입력: "))
# resident_number.remove("-")

# # 체크수 리스트 생성 
# check_number = [2,3,4,5,6,7,8,9,2,3,4,5]

# # 총합을 계산할 변수 초기값 설정
# total = 0
# count = 0
# # 주민번호를 하나씩 체크수에 곱하는 반복문 작성 
# for i in resident_number[:-1]: # 마지막 자리 제외
#     total += int(i) * check_number[count]
#     count += 1
        
# # 체크 계산

# if (11 - (total % 11)) % 10 == int(resident_number[-1]):
#     print("유효한 주민번호")

# else :
#     print("유효하지 않은 주민번호")
    