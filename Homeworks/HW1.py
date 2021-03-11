oddNum = list(range(0, 11, 2))
evenNum = list(range(1, 11, 2))

finalList = oddNum+evenNum
finalList.sort()
print(finalList)

multipliedList = [i*2 for i in finalList]
print(multipliedList)

for i in multipliedList:
    print("Data Type of Index",int(i/2),":", type(i))