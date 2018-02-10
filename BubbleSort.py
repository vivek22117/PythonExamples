import random
import math

numList = []
for i in range(6):
    numList.append(random.randrange(1, 10))

ln = len(numList) - 1

while ln > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        if numList[j] > numList[j + 1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Dont Swqp")
        j += 1
        for k in numList:
            print(k, end=" ,")
        print()
    print("END OF ROUND")
    ln -= 1
