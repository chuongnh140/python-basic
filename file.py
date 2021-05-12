file = open('file.txt','r')

f = file.readlines()

newList = []
for i in f:
    newList.append(i[:-1])

print(newList)


file.close()

