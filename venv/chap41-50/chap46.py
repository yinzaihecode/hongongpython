#chap46

# snake case
# i_love_you : 기본적으로 사용
# I_LOVE_YOU :상수


# camel
#ILoveYou : 클래스이름
#- iLoveYou - java
#- ILoveYou - python


class Student:
    def __init__(self, 이름, 나이):
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이

    def __del__(self):
        print("객체가 소멸되었습니다.")

    def 출력(self):
        print(self.이름, self.나이)
            
student = Student("윤인성", 3)
student.출력()
#클래스(틀)


# 3. 생성자 : def __init__(self)
# self means Student
# 4. 소멸자 : def __del__(self):

########### 정리 ##############

#1. 생성자
"""
    def __init__(self, 이름, 나이):
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이

"""

#2. 소멸자
"""
    def __del__(self):
        print("객체가 소멸되었습니다.")
"""

#3. 속성을 만드는 방법
"""
        self.이름 = 이름
        self.나이 = 나이
"""

#4, 함수를 만드는 방법
"""
    def 출력(self):
        print(self.이름, self.나이)
"""




