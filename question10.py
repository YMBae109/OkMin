# # 자연수 N을 입력 받는다.
# N = int(input("자연수 N을 입력하세요."))

# # 지정된 패턴으로 별(*)을 출력한다.


# for i in range(1, N+1):
#     # 시작 값, 끝 값 + 스텝 값
#     print("*" * i)

    
# for i in range(N-1, 0, -1):
#     # 시작 값, 끝 값, 스텝 값을 써서 출력
#     print("*" * i)
##################################################################

# 반복문 -> 반복해서 명령어를 실행한다.
#       -> 조건식이 "참"인 동안

# 파이썬에서 제공하는 반복문 종류 두 가지
# 1)for - 반복의 횟수가 명확히 정해져 있을 때
# 2)while - 반복의 횟수를 예측하지 못할 때

# N 값 입력
N = int(input("N 값을 입력 하세요"))

# 1 <=  "*" <= N, N번 반복하면 별을 1씩 증가하면서 출력
# 반복 (count)
#   count * "*"
for count in range(1,N):
    for _ in range(0, count):
        print("*", end = "")
    print()
# N -> 1, 1씩 감소.
# 반복 (count)
#   count * "*"   
for count in range(N, 0, -1):
        print("*" * count)
        
        
count = 1
while count <= 5:
    print(count) 
    count = count + 1
    
    