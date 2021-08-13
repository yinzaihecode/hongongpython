# https://www.youtube.com/watch?v=PuGnDXwe7uo&list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7&index=50
# getter setter
# https://www.youtube.com/watch?v=PuGnDXwe7uo&list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7&index=50
# 기본적인 속성 : Attribute
# 변화를 준 속성 : property


# code refactoring >>>

# 선언
class Rect:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise Exception("너비와 높이는 음수 불가.")
        self.__width = width
        self.__height = height # 변경 불가
    def get_width(self):
        return self.__width
    def set_width(self, width):
        if width <= 0:

        self.__width = width
    def get_area(self):
        return self.__width * self.__height



# __width -> 외부에서 변경 불가

# 호출
rect = Rect(20, 10)
rect.__width = -10
print(rect.get_area())