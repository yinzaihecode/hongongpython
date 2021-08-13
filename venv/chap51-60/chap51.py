# https://www.youtube.com/watch?v=o3mL6O8dQtE&list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7&index=53

import os
output = os.listdir

print("os.listdir",output)

# 폴더와 파일 구분

print("폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더",path)
    else:
        print("파일",path)

        #isdir -> dir이면  true,