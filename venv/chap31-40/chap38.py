def call_10_times(func):
    for i in range(10):
        func(i)


def print_hello(number):
    print("안녕하세요", number)
call_10_times(print_hello)


#filter함수, list등에서 필터링
# filter()


#Map 함수, param1로는 함수, param2는 이터러블즈(리스트..), 리스트를 기반으로 필터처리후 새로운 리스트를 만들어 리턴

print("list")
def even(number):
    return number % 2 == 0

a = list(range(100))
b= filter(even,a)

print(list(b))

for i in b:
    print(i)


# map()


#lambda
print("lambda")
c = list(range(100))
d = filter(lambda number: number % 2 == 0, c)
print(list(d))

