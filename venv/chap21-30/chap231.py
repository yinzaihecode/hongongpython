
# 배열에 있는 단을 전부 꺼내는걸 flating 이라고 함. 자주 사용

character = {
    "name":"기사",
    "level": 12,
    "items": {
        "sword" : "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세개 베기", "아주 세게 베기"]
}


for key in character:
    if type(character[key]) is dict: #딕셔너리에 있다면
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list: #리스트에 있다면
            for item in character[key]:
                print("{} : {}".format(key, item))
    else:
        print("{} : {}".format(key, character[key]))

# 캐릭터에 키에 키 EX items,swords, [key][k]