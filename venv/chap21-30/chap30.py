# https://www.youtube.com/watch?v=25P_0sQyiIM&list=PLCrpnnSGr_ETApnv5f26QHtbl14ShNL-5&index=31
# 리스트 내포

array = []
for i in range(0, 20, 2):
    array.append(i * i)

array2 = [j * j for j in range(0, 20, 2)]



print(array)
print(array2)


print("*---------------------*")

array_1 = [i for i in range(10)]
array_2 = [i for i in range(0, 10, 2)]
array_3 = [1 for i in range(10)]

print(array_1)
print(array_2)
print(array_3)


array_4 = [i for i in range(10) if i % 3 == 0]
print(array_4)

