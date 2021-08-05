def function():
    print("A")
    print("B")
    return
    print("C")
    print("D")

print(function())
print(function())

def sum_all(start, end):
    변수 = 0
    for i in range(start, end + 1):
        변수 += i
    return 변수

print(sum_all(1, 100))
print(sum_all(50,100))

# None
# 아무것도 리턴 안하면 None 출력
# EX) 딕셔너리.get("키") => 키에 해당하는 값이 없으면 None 출력.

def f_1(x):
    return (2*x) + 1

def f_2(x):
    return (x ** 2 ) + (2*x) + 1


print(f_1(10))
print(f_2(10))

def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return 변수


print(mul(5,7,9,10))




