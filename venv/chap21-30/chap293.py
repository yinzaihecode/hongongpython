a = [273, 103, 52, 32, 58]
enumerate_a = enumerate(a)


# for (i, element) in enumerate(a):
#     print("{}번째 요소는, {}입니다..".format(i,element))
#
#


for (i, element) in enumerate_a:
    print("{}번째 요소는, {}입니다..".format(i,element))


#------------------------실행되지 않음 ----------------------- #
for (i, element) in enumerate_a:
    print("{}번째 요소는, {}입니다..".format(i,element))
#------------------------실행되지 않음 ----------------------- #


"""
일회용 함수 : 제너레이터
현재 인덱스가 몇번째인가 확인 enumerate()
딕셔너리로 쉽게 반복문 작성 : items()
"""


# 기억 : for i, element in enumarate(리스트)
# enumerate는 1회용 함수.