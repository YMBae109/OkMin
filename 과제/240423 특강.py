# 정수 3개를 입력 받아서 제일 큰 값을 출력
'''max = -1

for trial_count in range(1, 4):
    msg = str(trial_count) + "번째 정수입력: "
    input_value = int(input(msg))
    
    if max < input_value:
        max = input_value

print(max)
        
 # 1이상 30이하의 정수 중에, 짝수이면서 5의 배수를 출력하시오.
 
for num in range(1,31):
    if num % 2 == 0: # if문 안에 if문 == and
        if num % 5 ==0:
            print(num,"\t",end="")'''
        
        
# 문제 3

# while True:
#     num = int(input("정수를 입력하세요"))
#     if num % 3 == 0 or num % 4 == 0:
#         break
    
#     print(num)

# for count in range(1, 10):
#     print(count // 5 + count % 5, "\t", end="") 
    

foo = "hello"

total = 0

for num in foo:
    total += 1
    
print(total)
