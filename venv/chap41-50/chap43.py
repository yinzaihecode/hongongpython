# try:
# except:
# finally(옵션, 필요에따라 사용)

try:
    number = int(input("> 정수 입력."))
    print("입력 값은{} 입니다.".format(number))
except:
    print("예외가 발생했습니다.")

finally:
    print("무조건적으로 실행됩니다.")



def test():
    print("test () 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행.")
        return
        print("try 구문의 return 키워드 뒤 입니다.")
    except:
        print("except 구문 실행")
    finally:
        print("finally 구문이 실행 되었습니다.")
    print("test() 함수의 마지막 줄 입니다.")

test()


# finally
# 1. file.close
# 2. db.close
# 3. cache clear

# 절대지켜




