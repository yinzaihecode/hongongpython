# https://www.youtube.com/watch?v=o3mL6O8dQtE&list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7&index=53

# 1. 모듈 읽기
import os


# 2. 폴더를 읽어 들이는 함수


def read_folder(path):
    print(path)
    output = os.listdir(path)
    #폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(path + "/" + item):
            #폴더라면 계속 읽기
            read_folder(path + "/" + item)
        else:
            #파일이라면 출력하기
            pass

#현재 폴더의 파일/폴더를 출력.
read_folder(".")

print("hellos")


for i in range(20):
    print("hello world!")
    print("hello debug")
