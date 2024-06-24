
# 미리 입력된 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 문자열 길이 함수
def str_length():
    # 문장 리스트 생성
    sentence_list = []
    word = ""

    for char in sentence:
        if char not in [' ', '\n']:
            word += char
        else:
            if word:
                sentence_list.append(word)
                word = ""

    if word :
        sentence_list.append(word)
    print(sentence_list)    
            


# 계속 반복
while True :
    input_user = "pos"

    print(len(sentence))

    # 문자열이 문장 내 있을 경우
    if input_user in sentence :
        
        # "검색된 문자열의 개수:"
        str_number = [ value for value in sentence_list if input_user == value ]
        print("검색된 문자열의 개수: ",len(str_number))
        
        # "검색된 문자열의 위치:"
        index_number = []
        for i in range(len(sentence)) :
            if sentence[i] == input_user[0] :
                index_number.append(i)
        
        print("검색된 문자열의 위치", index_number)
        
        # "단어의 개수 : 13"
        word_number = (len(sentence_list))
        print("단어의 개수: ",word_number)
        
        # "전체 문자 수 (총 문자수 - 띄어쓰기 - 개행문자)"
        # 띄어쓰기 개수 , 줄 개수
        space_number = [value for value in sentence if value == " "]
        number_of_lines = len(list(sentence.split("\n")))

        total_word_number = len(sentence) - len(space_number) - (number_of_lines - 1) 
        print("전체 문자 수: ",total_word_number)
        
        # "줄 수: 3"
        print("전체 문자 수: ",number_of_lines)
        
        break
    
    # 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받는다
    else :
        print("해당 문자열이 없습니다. 재입력 하세요")

