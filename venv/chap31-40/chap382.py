a = list(range(100))
print(list(map(lambda number: number * number, a))) # 람다
print([i * i for i in a if i % 2 == 0]) # 리스트 내포

b = list(range(100))
print(map(lambda x : x * x, b))

# <map object at 0x000001E4D2DE9070>
