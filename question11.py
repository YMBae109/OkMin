# 사용자에게 온도(섭씨) 입력받기

degree = float(input("현재 온도(섭씨)를 입력하세요: "))

# 입력 받은 온도에 따라, 야외 활동을 추천
# if serize 사용
if degree >= 30 :
    print(f"현재 온도: {degree:.1f}")
    print(f"추천 활동: 스키")
    
elif 20 <= degree < 30 :
    print(f"현재 온도: {degree:.1f}")
    print(f"추천 활동: 등산")
    
elif 10 <= degree < 20 :
    print(f"현재 온도: {degree:.1f}")
    print(f"추천 활동: 자전거 타기")
    
else :
    print(f"현재 온도: {degree:.1f}")
    print(f"추천 활동: 스키")