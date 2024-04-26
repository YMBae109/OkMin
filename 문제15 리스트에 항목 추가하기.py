# 빈 리스트를 생성
books = []

# 사용자 입력을 처리하는 루프를 시작
while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    if title == '종료': # 사용자가 종료 할 때 까지 진행
        break 
    books.append(title) 
    # 도서 제목을 리스트에 추가하는 코드
    # 리스트에 원소를 추가 할 때

# 최종 도서 목록 출력
print("도서 목록", books)

books = []

while True: