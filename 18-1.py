
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45 ,99]


A = [ value for value in scores if value >= 90 ]
B = [ value for value in scores if 70 <= value < 90 ]
C = [ value for value in scores if 50 <= value < 70 ]
D = [ value for value in scores if value < 50 ]

# 평균 값 계산

A_arg = sum(A) / len(A)
B_arg = sum(B) / len(B)
C_arg = sum(C) / len(C)
D_arg = sum(D) / len(D)

print(f"우수: {A} 평균: {A_arg}")
print(f"양호: {B} 평균: {B_arg}")
print(f"보통: {C} 평균: {C_arg}")
print(f"미홉: {D} 평균: {D_arg}")