

# 1. Format 함수

"".format(1,2,3,4)

print("{} {} {} {}".format(1,2,3,4))
print("{}년 {}월 {}일 {}요일".format(2019, 12, 9, "월"))

# 2. upper & lower 주어 동사형태로 사용

"hello".upper()
"hello".lower()

# 3 .strip

>>> "            answk       ".strip()
'answk'
>>> "            answk       ".lstrip()
'answk       '
>>> "            answk       ".rstrip()
'            answk'
>>>

# 4. find, rfind.
"가나다라마바사".find("라")
3
없으면 -1 리턴하는것도 중요한 부분.!

# 5. 연산자 in (글자도 연산자임)
"가" in "가나다라마바"
> true


# 6. split (s+v+o)
"10 20 30 40 50".split(" ")
>>> "10 20 30 40 50".split(" ")
['10', '20', '30', '40', '50']



a = input("> 1번째 숫자")
b = input("> 2번째 숫자")
print()

print("{} + {} = {}".format(a, b, int(a) + int(b)))

# 파괴적함수와 비파괴적함수 대부분의 함수는 원본을 변경하지 않음(비파괴적)

a = "hello"
a.upper()
b = a





