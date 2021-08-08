# 튜플이 리스트와 다른 기본적인 부분
# 1. 대괄호가 아닌 소괄호로 선언
# 2. 한번 선언하면 값을 바꿀 수 없음.


a = (1,2,3,4)
# a[0] = 100 # 불가


[a, b] = [10, 20]
[c, d] = [30, 40]


print(a,b,c,d)

# swap

print("스왑")
a, b = 10, 20
print(a, b)

a, b = b, a
print(a,b)


# 튜플을 리턴하는 함수.

a, b = 97, 40

print(a//b)
print(a%b)

print(divmod(a,b))
print(type(divmod(a,b)))

for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는, {}입니다.".format(i,value))



def test():
    return 10, 20

a, b =test()
print(a,b)


# 요소가 1개인 튜플

a = (123,)
# 콤마가 있다고해서 요소가 두개가아님..
# print(a[1]) 하면 에러남.




z = {
    (0, 0): 10,
    (0, 1): 20,
    (1, 0): 30,
    (1, 1): 40,
}

print(z)



# 튜플은 key로 올 수 있다.
# 메모화와 함께 사용.