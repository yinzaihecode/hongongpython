# break, continue
# https://www.youtube.com/watch?v=joyIjI_aM4I&list=PLCrpnnSGr_ETApnv5f26QHtbl14ShNL-5&index=28

i = 0
while True:
    print("{}번째 반복문 입니다.".format(i))
    i += 1


    input_text = input("> 종료하시겠습니까?(y)")
    if input_text in ["Y", "y"]:
        print("반복을 종료합니다.")
        break