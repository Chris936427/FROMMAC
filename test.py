import math
judge=input("请输入Y/N:   ")
if judge=='Y':
    result=math.pow(1.01,366)
    print(result)
else:
    result=math.pow(0.99,365)
    print(result)