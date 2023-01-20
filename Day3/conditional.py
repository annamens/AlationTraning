#if else condition
n=6

if n%2==0:
    print('even number')
elif n%2!=0:
    print('odd number')
else:
    print('number is 0')

n=24
a=True
for i in range(2,n//2):
    if(n%i==0):
        a = False
if a:
    print("prime")
else:
    print("not a prime")

lst = ['a','b','c',1,2,"python"]
for i in range(2,len(lst)):
    print(lst[i])
    #or
print('============================')
for i in lst:
    print(i,end=' ')
print('')
for i in range(20,10,-1):
    print(i, end=' ')
print('')
for j in range(1, 20,3):
    print(j,end=" ")