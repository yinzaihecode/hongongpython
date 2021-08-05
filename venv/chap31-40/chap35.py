# https://www.youtube.com/watch?v=rJALa9MW7M4&list=PLCrpnnSGr_ETApnv5f26QHtbl14ShNL-5&index=36

# n! = 1 * 2 * 3 * 4 * 5...(n - 2) * (n - 1) * n
#  재귀함수 참고 : https://youtu.be/apuLBFfGlQs
# 알고리즘 문제를 처음 푸실 때는 책 1-2권은 외운다는 생각으로 공부하시는 것이 좋습니다...!!

def factorial_1(n):
    변수 = 1
    for i in range(1, n + 1):
        변수 *= i
    return 변수


# 요즘 파이썬

memo = {1: 1, 2: 1}
def f(n):
    if n in memo:
        return memo[n] #조기리턴
    output = f(n-1) + f(n-2)
    memo[n] = output
    return output
print(f(150))