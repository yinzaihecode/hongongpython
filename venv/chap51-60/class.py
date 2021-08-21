# 클래스 > 최상위 부모 클래스 무조건 상속!!

class 부모:
    pass


class 자식(부모):
    pass


print(부모.mro())
print(자식.mro())

'''
[<class '__main__.부모'>, <class 'object'>]
[<class '__main__.자식'>, <class '__main__.부모'>, <class 'object'>]

Process finished with exit code 0
'''