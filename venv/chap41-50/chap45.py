# 클래스 도입.
# https://www.youtube.com/watch?v=A7d1mMdhePY&list=PLCrpnnSGr_ETApnv5f26QHtbl14ShNL-5&index=46
# 객체지향~?
# 객체의 정의 : object라고 불리움
# 1. 속성, 2. 행위를 가지는 대상
# 사람
# - 이름,키,나이,생년월일
# - x : 행위(?)

# students = [
#     { "name": "홍길동", "Korean": 87, "math": 98, "english": 88, "science":53},
#     { "name": "연하남", "Korean": 21, "math": 23, "english": 27, "science":42},
#     { "name": "민구지", "Korean": 34, "math": 53, "english": 72, "science":64},
#     { "name": "나천재", "Korean": 57, "math": 98, "english": 85, "science":85},
#     { "name": "홍인수", "Korean": 17, "math": 87, "english": 47, "science":74},
#     { "name": "배홍동", "Korean": 86, "math": 45, "english": 86, "science":26},
#     { "name": "삼겹살", "Korean": 60, "math": 79, "english": 90, "science":85},
#
# ]

#Key는 함수의 param으로 선언.
#Value는 함수 호출시 넣어서 호출.



def 학생_생성(name,korean,math,english,science):
    return{
        "name": name,
        "korean": korean,
        "math" : math,
        "english" : english,
        "science": science,
    }




students = [
    학생_생성("홍길동", 92,37,54,32),
    학생_생성("연하남", 92,42,99,88),
    학생_생성("남민구", 92,77,88,57),
    학생_생성("지사인", 92,66,88,99),
    학생_생성("주윤영", 92,65,86,57),
]



print("*---------*")
print(students)

# 위에 딕셔너리만 드는 함수



def 총점(student):
    return student["korean"] + student["math"] + \
        student["english"] + student["science"]

def 평균(student):
    return 총점(student) / 4

def 출력(student):
    print(student["name"], 총점(student), 평균(student), sep="\t")


# 학생을 한명씩 반복.
print("이름", "총점", "평균", sep="\t")
for student in students:
    출력(student)
