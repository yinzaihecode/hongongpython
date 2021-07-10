# chap24.py
# 딕셔너리 안전하게 출력하기. 키에러방지 조건문

dictionary = {

    "이름": "구름",
    "종족": "강아지"

}


print(dictionary["이름"])
print(dictionary["종족"])
print(dictionary["직위"])
```python

Traceback (most recent call last):
  File "D:/hongongpython/venv/chap21-30/chap24.py", line 14, in <module>
    print(dictionary["직위"])
KeyError: '직위'
구름
강아지


print(dictionary["이름"])
print(dictionary["종족"])
print(dictionary["직위"])

이 코드 기억
if "나이" in dictionary:
    
딕셔너리에서 get함수사용.
아니면 dictionary.get 


```
> 데이터를 쭉 끌고와서 
> 

```python
if "나이" in dictionary:
    print(dictionary["나이"])
else
    print("없는 키 입니다.")
```


