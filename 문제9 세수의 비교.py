# # 사용자로부터 세 개의 정수를 입력 받는다. #print,input,int 외에 사용금지

# inputValue1 = int(input("첫 번째 수 입력: "))
# inputValue2 = int(input("두 번째 수 입력: "))
# inputValue3 = int(input("세 번째 수 입력: "))

# # 모든 수가 같을 경우 코드 작성 후 출력

# if inputValue1 == inputValue2 == inputValue3:
#     print("모든 수가 같습니다.")
    
# # 두 수가 같을 경우 코드 작성 후 출력
# elif inputValue1 == inputValue2 :
#     print(f"두 수가 같습니다. ({inputValue1}와 {inputValue2})")
# elif inputValue2 == inputValue3 :
#     print(f"두 수가 같습니다. ({inputValue2}와 {inputValue3})")
# elif inputValue1 == inputValue3 : 
#     print(f"두 수가 같습니다. ({inputValue1}와 {inputValue3})")
    
#  # 모든 수가 다를 경우 코드 작성 후 출력
# else :
#     print(f"모든 수가 다릅니다. 가장 큰 수는 {max(inputValue1,inputValue2,inputValue3)}입니다.")
    
    
#교수님 버젼-------------------------------------------------------------------------------------

# # 정수 3개를 입력 받는다.

# a = int(input("첫 번째 입력 값 : "))
# b = int(input("두 번째 입력 값 : "))
# c = int(input("세 번째 입력 값 : "))

# # 입력 값이 모두 같으면, "모든 수가 같습니다." 출력
# if a == b and b == c and a == c :
#     print("모든 수가 같습니다.")

# # 입력 값이 두 개가 같으면
# # 1) "두 수가 같습니다." 출력
# elif a == b or b == c or c == a :
#     print("두 수가 같습니다.")
# # 2) 두 수도 출력
#     if a == b:
#         print(a, ":", b)
#     elif b == c:
#         print(b, ":", c)
#     else :
#         print(c, ":", c)

# # 입력 값이 모두 다르면,
# # 1) "모든 수가 다릅니다."
# else :
#     print("모든 수가 다릅니다.")
# # 2) 가장 큰 값을 출력한다.
#     if a > b and a > c:
#         print(a, "가 최대 값")
#     elif b > a and b > c:
#         print(b, "가 최대 값")
#     else :
#         print(c, "가 최대 값")
        
        
#3회차#######################################################

# 사용자로 부터 세 개의 정수를 입력 받는다.

a = int(input("첫 번째 수 입력: "))
b = int(input("두 번째 수 입력: "))
c = int(input("세 번째 수 입력: "))

# 모든 수가 같으면 "모든 수가 같습니다." 출력
# a == b == c 

if a == b and a == c and b == c:
    print("모든 수가 같습니다.")

# 두 수가 같으면, "두 수가 같습니다."와 같은 두 수도 출력
# a == b or a == c or b == c 

elif a == b or a == c or b == c:
# 두 수도 출력 
    if a == b:
        print("두 수가 같습니다.",a,":",b)
    elif a == c:
        print("두 수가 같습니다.",a,":",c)
    else:
        print("두 수가 같습니다.",b,":",c)
        
# 모든 수가 다르면, "모든 수가 다릅니다. 가장 큰수는  입니다." 출력
# a > b and a > c, b > a and b > c and c > a and c > b

else : 
    if a > b and a > c :
        print("모든 수가 다릅니다. 가장 큰수는",a,"입니다.")

    elif b > a and b > c :
        print("모든 수가 다릅니다. 가장 큰수는",b,"입니다.")

    else :
        print("모든 수가 다릅니다. 가장 큰수는",c,"입니다.")
