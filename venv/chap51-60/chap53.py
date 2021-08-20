#BS 모듈 = 라이러리
#Flask 모듈 = 프레임워크

#라이브러리 : 정상적인 제어 방법으로 사용하는 모듈
# 프레임워크 : 제어 역전(IoC)이 일어나는 모듈
# 모듈이 개발자의 코드를 사용한다 -> 제어역전(IoC) 면접.



from flask import Flask #클래스
app = Flask(__name__) #클래스를 사용하여 객체 만들고 app,

@app.route("/") # 데코레이터
def hello():
    return "<H1>Hello, World.<H1>"


'''윈도우
set FLASK_APP=파일이름.py
set FLASK_APP=chap53.py
flask run
'''

'''mac
export FLASK_APP=파일이름.py
flask run
'''
