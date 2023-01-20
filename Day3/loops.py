

fruits = ['apple','banana','mango','grapes','oranges']
#for i in fruits:
  #  print(i)
for i in range(1,len(fruits)):
    print(fruits[i])
print('**************')
i=0
while i<=len(fruits):
    print(fruits[i], end='')
    j=1
    while j<=len(fruits):
        print(' is a fruit')
        j=j+1
    i=i+1
