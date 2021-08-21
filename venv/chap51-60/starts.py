print(__name__)
#1. __main__


import my_module

print(my_module.a)
print(my_module.b)
print(my_module.c())

if __name__ == "__main__":
    print("엔트리포인트입니다. A.") #6
#처음 진입한 파일 = 진입점 = 엔트리 포인트 = 메인

#
# python 파일.py
# 파일 > 모듈 > 모듈 > 모듈
# 파일: 진입점(엔트리 포인트)
# 메인파일
