# 제너레이터
# 이터레이트 직접 만들 때 사용하는 구문
# 함수 내부에 yield 라는 키워드가 포함되면 해당 함수는 제너레이터가 됩니다:

def 함수():
    print("출력 A")
    yield 100 # 멈춤
    print("출력 B")
    yield 200
    print("출력 C")
    yield 300
    print("출력 D")
    yield 400

제너레이터 = 함수()
next(제너레이터)

for i in 제너레이터:
    print(i)


# 일회용 함수
numbers = [1,2,3,4,5]
for i in reversed(numbers):
    print(i)

