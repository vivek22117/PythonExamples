import os

# with open("myData.txt", mode="w", encoding="utf-8") as myFile:
# myFile.write("Some random text\nMore to More data\nAnd some file data only exit")
# lineNum = 1

with open("myData.txt", encoding="utf-8") as myFile:
    # print(myFile.read())
    lineNum = 1

    while True:

        line = myFile.readline()
        if not line:
            break
        print("LineNumber: ", lineNum)
        words = line.split()
        print("Number of words: ", len(words))
        countNum = 0
        for word in words:
            for char in word:
                countNum += 1

        avgWordSize = countNum / len(words)
        print("Avg length of words is {:.2}".format(avgWordSize))

        lineNum += 1
