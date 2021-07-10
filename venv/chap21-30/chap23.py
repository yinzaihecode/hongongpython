리스트 = []
리스트 = [
    1,
    2,
    3
]

리스트[0] # 인덱스

딕셔너리 = {
    "키A": "값A",
    "키b": "값b",
    "키c": "값c",
    "키d": "값d",
    "문자열": "값",
    273 : [1,2,3,4],
    True: False
}

딕셔너리["키A"] # 키

print(딕셔너리["문자열"])
print(딕셔너리[273])
print(딕셔너리[True])

# 딕셔너리 값 변경
딕셔너리["문자열"] = "값값"

# 반복문
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

# 지우기

# del 딕셔너리["키"]



# 딕셔너리의 값 확인하기
# 1. in 키워드로 확인
# 2. get 함수 사용
dictionary = {
    "이름": "구름",
    "종족": "강아지"
}

dictionary["이름"] #"구름"



if "나이" in dictionary:
    print(dictionary["나이"])
else:
    print("없는 키 입니다.")

# dictionary.get("이름") -> "구름"
# dictionary.get("나이") -> None



if dictionary.get("나이") == None:
    dictionary.get("나이")
else:
    print("없는 키 입니다.")


# 딕셔너리와 리스트의 조합

pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 2},
]
print("pets는 우리 동네 애완 동물들. : {}".format(pets))

for pet in pets:
    print(pet)

for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

# 딕셔너리 출력할때 키 값 넣는거 까먹지말기


numbers = [1,2,6,8,6,4,3,1,2,3,4,5,6,7,8,7,3,2,6,8,9,4,1,3,5,3,2,1]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)


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