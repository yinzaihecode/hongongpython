key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

# 작성
# list 2개 이상 있을 경우 아래와 같이 range 하나 껴서 리스트 돌릴것
# 담는 그릇은 char 딕셔너리
# 반복하는건 배열
for i in range(len(value_list)):
    character[key_list[i]] = value_list[i]

# 최종 출력
print(character)
