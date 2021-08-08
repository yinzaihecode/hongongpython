class 학생:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def 총점(self):
        return self.korean + self.math + \
            self.english + self.science
    def 평균(self):
        return self.총점() / 4
    def 출력(self):
        print(self.name, self.총점(), self.평균(), sep="\t")

    # 학생리스트 선언

students = [
        학생("홍길동", 92, 37, 54, 32),
        학생("연하남", 92, 42, 99, 88),
        학생("남민구", 92, 77, 88, 57),
        학생("지사인", 92, 66, 88, 99),
        학생("주윤영", 92, 65, 86, 57),
]

print("이름","총점","평균", sep="\t")

for student in students:
    student.출력()


# 클래스구문을 사용했을때 차이..!!
# 프로그래밍 언어는 영어의 어순을 따라가게 됨

# 주어 + 동사 + 목적어 순합
# 객체 지향 --> 주어가 행위를 한다.
# - 학생.출력()
# - 학생.평균()
# - 학생.총합()
# 객체 지향끼리 상호작용
# 클래스를 구현하고 그 기반으로 코드를 작성하겠다 -. 객체지향 하겠다.
# 클래스를 사용함으로써 객체지향..!!

