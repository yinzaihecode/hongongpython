# https://www.youtube.com/watch?v=PuGnDXwe7uo&list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7&index=50
# getter setter

# 선언
class Rect:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise Exception("너비와 높이는 음수 불가.")

        self.__width = width
        self.__heigh = height

    def get_area(self):
        return self.width * self.height

# __width -> 외부에서 변경 불가

# 호출
rect = Rect(20, 10)
rect.width = -10
