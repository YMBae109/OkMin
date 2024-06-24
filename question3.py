# 1제곱미터(m²) = 10.7639 평방피트 (ft²)
# 1에이커(ac) = 4046.86 제곱미터 (m²)
# 변환 함수 선언
def convert_to_square_feet(square_meters):
    ft = square_meters * 10.7639
    return(ft)

def convert_to_acres(square_meters):
    acres = square_meters / 4046.86
    return acres

# 사용자로 부터 토지의 면적을 입력 받는다

square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 변환 함수 호출과 결과 출력
if square_meters < 0:
    print("잘못된 입력입니다.")

else :
    print(f"{square_meters}제곱미터는 {convert_to_square_feet(square_meters)} 평방피트입니다.")
    print(f"{square_meters}제곱미터는 {convert_to_acres(square_meters)} 에이커입니다.")


# def convert_to_square_feet(sqaure_meters):
#     # 1m^2 = 10.7639 ft^2
    
# def convert_to_acres(sqaure_meters):
#     # 1ac = 4046.86 m^2
    

# sqaure_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))


# # 면적 값이 음수일 경우 에러
# if sqaure_meters < 0 :
#     print("잘못된 입력")
    
# else :


###################3회차############################################
####################################################################

# 