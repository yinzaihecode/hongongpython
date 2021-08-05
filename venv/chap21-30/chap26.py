# while True:
#     print("hello")


i = 0
while i < 10:
    print(i, end=" ")
    i +=  1

import time

firstTime = time.time()
while firstTime + 5 >= time.time():
    pass
print("프로그램이 종료되었습니다.")
