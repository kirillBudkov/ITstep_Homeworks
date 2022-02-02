task 1
param=int(input('enter parameter: '))
for i in range(1, param+1):
    print('*'*i)
task 2
inp1 = int(input('enter start of range: '))
inp2 = int(input('enter end of range: '))
_sum=0
for i in range(inp1, inp2+1):
    if i%5==0 and i%2!=0:
        _sum+=i
print(_sum)
