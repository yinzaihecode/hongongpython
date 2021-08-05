def print_n_times(value, n):
    for i in range(n):
        print(value)


#print_n_times("안녕하세요!")
print_n_times("안녕하세요!", 5)


print("안녕하세요!")
print("안녕하세요!", 2)
print("안녕하세요!", 4, 100)


#  가변 매개변수
# 한 함수에 가변 매개변수 딱 하나,
# 가변매개변수는 무조건 맨 마지막에.

def function(param1, param2, *args):
    print_n_times(param1)
    print_n_times(param2)
    print_n_times(args)


