# chap39.py


# 어떤 대상
# - 텍스트 파일: 텍스트에디터로 열 수 있음
# - 바이너리 파일: 에디터로 열수 없음(이미지,동영상,워드,엑셀,pdf...) 메모장 사용불가


# 어떻게 다룰것인가.
# - 쓰기
#     -새로(write) : w
#     -읽는 파일 뒤에(append) : a
# - 읽기(read) : r


# 1. open, 매개변수 2개
file = open("test.txt", "a")
file.write("안녕하세요.")
file.close()

##2 with open open and close)
with open("test.txt", "a") as file:
    file.write("안녕하세요.")

file = open("test.txt", "r")
print(file.read())
file.close()

# with 구문

# with 뒤에 파일 오픈 as file:
