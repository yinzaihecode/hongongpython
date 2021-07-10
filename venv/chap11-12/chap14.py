import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은 {}시, {}분으로 오전입니다.".format(now.hour, now.minute))
if now.hour > 12:
    print("현재 시간은 {}시, {}분으로 오후입니다.".format(now.hour, now.minute))

# 홀짝
# 끝자리

number = input("정수를 입력 해 주세요.")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다.")

if last_character in "13579"
    print("홀수입니다.")

if int(number % 2 == 0):
    print("짝수입니다.")
if int(number % 2 != 0):
    print("홀수입니다.")
