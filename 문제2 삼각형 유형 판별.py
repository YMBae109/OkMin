# 사용자에게 세 개의 수를 변의 길이로 하는 수 입력받는다.

length1 = int(input("첫 번째 변의 길이를 입력하세요: "))
length2 = int(input("두 번째 변의 길이를 입력하세요: "))
length3 = int(input("세 번째 변의 길이를 입력하세요: "))

# 세 변의 길이가 삼각형을 형성할 수 있는 조건인지 검사
if length1 + length2 > length3 and length2 + length3 > length1 and length1 + length3 > length2 :
    # 형성 할 수 있다면 삼각형의 유형을 출력
    if length1 == length2 == length3 :
        print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")
    elif length1 == length2 or length2 == length3 or length1 == length3 :
        print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")
    else :
        print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")   
else :
    # 나머지 삼각형을 형성할 수 없다는 문구 출력
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")


# 삼각형 세변의 길이 입력


# 삼각형을 만들 수 있다.

    # 정삼각형 : 세 변의 길이가 모두 같다. 

    # 이등변삼각형 : 두 변의 길이가 같다.

    # 부등변삼각형 : 세변의 길이가 같지 않다.

# 삼각형을 만들 수 없다. : 두 변의 길이의 합이 나머지 변보다 작거나 같다.