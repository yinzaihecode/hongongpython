# 함수 봉구


a = min([273, 52, 32, 57, 103])
b = max([273, 52, 32, 57, 103])
c = sum([273, 52, 32, 57, 103])

a = [0, 1, 2, 3, 4, 5]
reversed_a = reversed(a)

for i in reversed_a:
    print(i, end=" ")
print()

for i in reversed_a:
    print(i, end=" ")

print(reversed_a)

print(a)
print(b)
print(c)

"""
리스트에 적용할 수 있는 기본함수 : min(), max(), sum()
리스트 뒤집기 : reversed()
현재 인덱스가 몇 번째인지 확인 하기 : enumerate()
딕셔너리로 쉽게 반복문 작성하기 : items()


1. list(reversed(리스트)) : 리스트 역으로 돌리기
for i in reversed(리스트): 반복문에 적용
"""
