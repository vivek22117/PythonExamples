# create dictionary

# print("ENter value to create dictionary: ")
# n = int(input())
# d = dict()
# for i in range(1, n+1):
#     d[i] = i*i
#
# print(d)

# #create tuple
#
# values = input("ENter some cs values ")
# list = values.split(",")
# tuple = tuple(list)
# print(list, tuple)

list = []
for i in range(2000, 3201):
    if (i % 6 == 0) and (i % 3 != 0):
        list.append(i)

print(list)
