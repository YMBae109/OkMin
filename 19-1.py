
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45 ,99, 82, 67, 50, 77, 89]

A = [ value for value in scores if value >= 90 ]
B = [ value for value in scores if 80 <= value < 90 ]
C = [ value for value in scores if 70 <= value < 80 ]
D = [ value for value in scores if 60 <= value < 70 ]
F = [ value for value in scores if value < 60 ]


for _ in A :
    A_arg = sum(A) / len(A) 
    A_ko = len(A)
    _ = "*" 
print(f"A 등급: 평균 점수 = {A_arg:.2f}\n{_ * A_ko}({A_ko}명)")

for _ in B :
    B_arg = sum(B) / len(B)
    B_ko = len(B)
    _ = "*"
print(f"B 등급: 평균 점수 = {B_arg:.2f}\n{_ * B_ko}({B_ko}명)")

for _ in C :
    C_arg = sum(C) / len(C)
    C_ko = len(C)
    _ = "*"
print(f"C 등급: 평균 점수 = {C_arg:.2f}\n{_ * C_ko}({C_ko}명)")

for _ in D :
    D_arg = sum(D) / len(D)
    D_ko = len(D)
    _ = "*"   
print(f"D 등급: 평균 점수 = {D_arg}\n{_ * D_ko}({D_ko}명)")

for _ in F :
    F_arg = sum(F) / len(F)
    F_ko = len(F)
    _ = "*"  
print(f"F 등급: 평균 점수 = {F_arg}\n{_ * F_ko}({F_ko}명)")


found = False  # 초기값은 False

while not found:
    user_input = input("정답을 입력하세요: ")
    if user_input == "정답":
        found = True  # 조건을 만족하면 플래그를 True로 설정
        print("정답을 맞추셨습니다!")
    else:
        print("다시 시도해 보세요.")