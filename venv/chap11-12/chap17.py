bool("")
bool(())
bool({})
bool({"a":"a"})

Type "help", "copyright", "credits" or "license" for more information.
>>> bool("")
False
>>> bool(())
False
>>> bool({})
False
>>> bool({"a":"a"})
True


if number != 0:
    print("처리를 한다.")
else:
    print("0이 나왔습니당.")


# bool의 쓰임 -> true false 분기
# pass는 아무것도 없을때 아무것도 안적을때

message = ""

if message:
    print("처리를 한다.")
else:
    print("메시지를 입력해주세요.")


number = 0 # 나중에!

if number != 0:
    #이런처리
    pass
else:
    pass




