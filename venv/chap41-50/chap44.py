try:
    a = [273, 103,52,57,100]
    number = int(input("정수입력(0~4까지 입력해주세요.)>"))
    print(a[number])

except ValueError as exception:
    print("값에 문제가 있습니다.")
except IndexError as exception:
    print("0~4까지 입력해주세요.")
except Exception as exception:
    print("알 수 없는 예외가 발생했습니다.")
    #Exception은 최상단 예외처리, 맨 마지막에 기술
    #개발자에게 메일을 보낸다.


#예외객체 사용
#except 예외의종류 as 변수로사용할이름:
#with open() as 변수로 사용할 이름:

#raise  키워드

#raise 예외객체
#raise Exception("안녕하세요.")
#예외를 강제로 발생 -> 언제사용하니?
#개발자를 위한 라이브러리 만들때,...
# github 텐서플로우 가서 raise 검색!
# 유명 라이브러리 깃헙 가서 검색해보는 습관 들이기.
# try, except finally -> 처럼..!
