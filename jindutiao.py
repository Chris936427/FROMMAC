import time
scale=10
char='执行开始'
print("{0:$^20}".format(char))
for i in range(scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    print("\r%{:^3.0f}[{}->{}]".format(c,a,b),end='')
    time.sleep(1)
print()
print("{0:$^20}".format('执行结束'))
