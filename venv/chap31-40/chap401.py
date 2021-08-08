# chap401.py

numbers = [1,2,3,4,5,6]
print("::".join(
    map(str, numbers)
))


numbers = list(range(1, 10 + 1))
print("#홀수만 추출하기")
print(list(filter(lambda x: x% 2 == 1, numbers)))
print()


print("3이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("#제곱해서 50 미만 추출하기")
print(list(filter(lambda x: (x ** 2) < 50 , numbers)))
print()


#numbers를 map str함수로 새로운 리스트 생성.


"""
>  print("::".join(numbers))
TypeError: sequence item 0: expected str instance, int found
# 형변환 어떻게할것인가? map함수 사용.
"""

