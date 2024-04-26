import random

# 중복 값이 없는 정수의 개수
trial_num = int(input("(1-100)입력"))

# 중복 값이 없는 정수를 저장할 List
made_list = []

# trial_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장
for trial_count in range(0, trial_num):
    
    # 중복 값 검사를 위해서
    while True:
        random_num = random.randint(1,100)
    
        found_duplication = False 

        for made_index in range(0, trial_count):
            # 중복값이 있으면
            if made_list[made_index] == random_num:
                found_duplication = True
                break
        
        if not found_duplication:
            made_list.append(random_num)
            break

print(made_list)

while True:
    input_index = int(input("index : "))
    
    if 0 <= input_index < len(made_list):
        print("원소 값 : ", made_list[input_index]) 
        break
    
# 이해를 하려면 분석을 하고, 이 문제만 풀어보자


import random

N = 5

list = []