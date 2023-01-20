#f = open('newFile','w')
#f.write('first line')
#f.write('second line')
f = open('newFile','r')
print(f.readlines())

g = open('git-commands.txt','r')

for data in g:
    print(data)