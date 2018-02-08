# empty_List = []
#
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         empty_List.append(str(i))
#
# print(",".join(empty_List))

# def factorial(number):
#     if(number == 0):
#         return 1
#     else:
#         return number * factorial(number-1)
#
# print("ENter an interger value between 1 to 99: ")
# num = int(input())
# print(factorial(5))


# class Example():
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input("ENter the string value :")
#
#     def printString(self):
#         print(self.s.upper())
#
#
# x = Example()
#
# x.getString()
# x.printString()

def pair_finder(arr1, k):
    if len(arr1) < 2:
        return print("Too Small")

    seen = set()
    output = set()

    for num in arr1:
        value = k - num
        if value not in seen:
            seen.add(num)
        else:
            output.add((min(value, num), max(value, num)))

    print("\n".join(map(str, output)))


pair_finder([1, 2, 3, 2], 4)
