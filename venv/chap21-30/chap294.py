a = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
    "key_4": "value_4",


}


#전형적으로 딕셔너리 값 빼내기
for key, value in a.items():
    print("{}키 값은 {}입니다.".format(key, value))