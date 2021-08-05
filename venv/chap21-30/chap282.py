max_value = 0
a = 0
b = 0
for i in range(1, 99 + 1):
    j = 100 - i
    print(i, j)
    # 최댓갑 구하기
    if max_value < i * j:
      subtotal =  i * j

max_value = current
print("최대가 되는 경우: {} * {} * {}".format(a, b, max_value))
print(subtotal)
