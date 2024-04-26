# pop을 잘 쓰는 방법

import random
n = 5 
max_num = 6
# List comprehension
sample_list = [ value for value in range(1, max_num) ]

random_list = []

for trial_count in range(0, n):
    random_index = random.randint(0, len(sample_list) - 1)
    random_num = sample_list.pop(random_index)
    random_list.append(random_num)
    
print(random_list)

# 난수를 index 값으로 설정하고, pop을 사용하여 중복체크 연산 필요없이
# 중복되지 않은 리스트를 생성한다

bar = [1,2,3,4,5]
bar.clear()
print(bar) # 리스트의 원소만 삭제되고 리스트는 유지

foo = [1,2,3,4,5]
del foo # 접근이 불가 -> 좀비 메모리 -> Garbage collector