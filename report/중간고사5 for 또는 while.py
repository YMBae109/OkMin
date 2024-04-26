
count = int(input())

for i in range(count, 0, -1):
    space = ' ' * i
    print(space,end="")
    star = '*' * i
    print(star)
    count += 1
