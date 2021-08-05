# 1~100 중 / 2진수 / 0이 하나만 포함된 숫자의 합

output = 0
for i in range(1, 100 + 1):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i, i))
        output += i
print("합계 : {}".format(output))


print("-------------------")
print("리스트 내포")


output2 = [j for j in range(1,100,1) if "{:b}".format(j).count("0") == 1]
for j in output2:
    print("{} : {}".format(j, "{:b}".format(j)))
print("합계: {}".format(sum(output2)))
