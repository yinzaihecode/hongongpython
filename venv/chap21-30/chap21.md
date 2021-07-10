# 문제 1
다음 함수 결과 기재

```python
list_a=[0,1,2,3,4,5,6,7]

list_a.extend(list_a)

>>> list_a
[0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]


list_a.append(10)
[0, 1, 2, 3, 4, 5, 6, 7, 10]

list_a.insert(3,0)
[0, 1, 2, 0, 3, 4, 5, 6, 7]

list_a.remove(3)
[0, 1, 2, 4, 5, 6, 7]

list_a.pop(3)
>>> list_a.pop(3)
3

>>> list_a
[0, 1, 2, 4, 5, 6, 7]

list_a.clear()
>>> list_a
[0, 1, 2, 4, 5, 6, 7]
>>> list_a.clear()
>>> list_a
[]


```
---

```python

numbers = [273,231,645,236,53,674,134,754]

for number in numbers:
    if number >= 0:
    print("100 이상의 수: {}".format(number))


```
 
# 사칙연산중 / 연산자는 float을 리턴함
> int는 // 연산자 사용할것
> 

---

# 홀짝 문제
```python

numbers = [273,543,12,3,64,210,69]

HZ = ["짝수","홀수"]

for number in numbers:
    print("{}는, {}입니다.".format(number, HZ[number % 2]))
```

```python
273는, 홀수입니다.
543는, 홀수입니다.
12는, 짝수입니다.
3는, 홀수입니다.
64는, 짝수입니다.
210는, 짝수입니다.
69는, 홀수입니다.
```

---


