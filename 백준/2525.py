
# 시 분을 입력 받는다
H, M = map(int, input().split())

# 소요시간을 입력 받는다
time = int(input())

# if 문 활용하여 출력

if M - time >= 0 :
    if time > 59:
        print(H, H + (time // 60)) 
    else : 
        print(H, M - time)

else : 
    if M - time