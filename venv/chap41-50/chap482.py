class Rect:
    def __init__(self, width, heigh):

    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self,width):
        if width <= 0:
            raise Exception("너비는 음수가 나올 수 없습니다.")
        self.__width = width

    @property
    def get_height(self):
    @height.setter

    def set_height(self, height):
    def get_area(self):

rect = Rect(10, 10)
rect.width = - 10
print(rect.get_height())