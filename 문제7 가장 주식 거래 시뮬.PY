# # 사용자 4가지 정보 입력
# seed_money = int(input("초기 자본금을 입력하세요: "))
# stock_price_buy = int(input("주식 가격을 입력하세요: "))
# stock_count = int(input("구매할 주식 수를 입력하세요: "))
# stock_price_sell = int(input("판매할 때의 주식 가격을 입력하세요: "))

# # 주식 구매 후 남은 자본금
# rest_money = seed_money - (stock_price_buy * stock_count)

# # 주식 판매시 금액
# sale_money = (stock_count * stock_price_sell) - (stock_price_buy * stock_count)

# print(f"구매 후 남은 자본금: {rest_money:.2f}")
# print(f"예상 이익: {sale_money:.2f}")

# # 주식 판매 시 예상 이익 또는 손실 - 계산식 작성

# if sale_money > 0 :
#     print("예상되는 이익입니다.")
# elif sale_money < 0 :
#     print("예상되는 손실입니다.")
# else : 
#     print("손익분기점")
    
    
######2회차###########################################################

# 주식 거래 시뮬레이션을 위한 함수 정의
def stock_simul():
    # 사용자의 정보 입력 받기
    seed_money = int(input("초기 자본금을 입력하세요: "))
    stock_price_buy = int(input("주식 구매 가격을 입력하세요: "))
    stock_count = int(input("구매할 주식 수를 입력하세요: "))
    stock_price_sell = int(input("판매할 때의 주식 가격을 입력하세요: "))

    # 구매 후 남은 자본금 계산
    remaining_money = seed_money - (stock_price_buy * stock_count)
    # 주식 판매 시 예상 이익 계산
    expected_profit = (stock_price_sell * stock_count) - (stock_price_buy * stock_count)

    # 구매 가능 여부 확인 및 결과 출력
    if seed_money < (stock_price_buy * stock_count):
        return "자본금이 부족하여 주식 구매가 불가능합니다."
    else:
        print(f"구매 후 남은 자본금: {remaining_money}원")
        print(f"예상 이익: {expected_profit}원")

        # 이익이 발생했는지 손실이 발생했는지 판단
        if expected_profit > 0:
            return "예상되는 이익입니다."
        elif expected_profit < 0:
            return "예상되는 손실입니다."
        else:
            return "본전입니다."

# 함수 실행 후 결과 출력
result = stock_simul()
print(result)
