# try except 구문.
# print(float(input(">>> 숫자를 입력해주세요.")) ** 2)


while True:
    try:
    # 예외가 발생할 수 있는 가능성이 있는 코드.
        print(float(input(">>> 숫자를 입력해주세요.")) ** 2)
        break
    except:
        # 에외가 발생했을 때 실행할 코드.
        print("숫자를 입력해주세요.")
        pass



list_input_a = ["32","456","2013","990","스파이"]

list_numbuer = []
for item in list_input_a:
    #숫자로 변환하여 리스트로 추가.
    try:
        float(item) #예외 발생시, 알아서 다음으로 진행
        list_numbuer.append(item)
    except:
        pass

#출력
print("{} 내부에 있는 숫자는.".format(list_input_a))
print("{} 입니다.".format(list_numbuer))

