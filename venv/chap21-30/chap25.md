# range

> range <= 자료형
> 

---

# range(0, 0, 0)
## range(시작, 끝, 단계)
## range(시작, 끝) # 단계 =1 생략
## range(끝) #시작 =0과 단계 1 생략

---

```python
# 결과 기억

>>> range(0,10,1)
range(0, 10)
>>> list(range(0,10,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> list(range(0,10,3))
[0, 3, 6, 9]
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>


```

# 1. 리스트와 조합해서 사용하는 경우

```python
array = [283,232,12,32,56]

i = 0
for element in array:
    print("{} : {}".format(i, element))

print("===========")


for j in range(len(array)):
    print("{} : {}".format(i, array[j]))



```

 
# 2. 역 반복문 - reversed 함수 사용.
# 많이 사용! 
```python
for k in reversed(range(0,10)):
    print(k)
```