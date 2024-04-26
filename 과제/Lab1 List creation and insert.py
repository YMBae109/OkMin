# shopping_list 빈 리스트 생성
shopping_list = []

# 품목을 리스트에 추가
shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
shopping_list.append('apple')

# 쇼핑리스트 출력
print("현재 쇼핑 리스트:",shopping_list)

# 리스트 추가
shopping_list.insert(0,'toilet paper')
shopping_list.insert(2,'orange juice')

# 한 번의 연산으로 리스트 추가
additional_list = ['chicken', 'rice']
final_list = shopping_list + additional_list

# 최종출력
print("최종 쇼핑 리스트:",final_list)

