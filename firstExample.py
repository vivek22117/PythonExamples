# name = input("what is your name ")
#
# print(" hello " + name)

# num1, num2 = input("enter 2 numbers: ").split()
#
# num1 =int(num1)
# num2 = int(num2)
#
# sum = num1 + num2
#
# print("{} + {} = {}".format(num1, num2, sum))


# miles = input("enter distance in miles: ")
# miles = int(miles)
# kilometers = miles * 1.609
# print("{} miles is equal to {} kilometer ".format(miles, kilometers))

# num1, operator, num2 = input("Enter calculation: ").split()
# num1 = int(num1)
# num2 = int(num2)
#
# if operator == "+":
#     print("{} + {} = {}".format(num1, num2, num1+num2))
# elif operator == "-":
#     print("{} + {} = {}".format(num1, num2, num1 - num2))
# elif operator == "*":
#     print("{} * {} = {}".format(num1, num2, num1 * num2))
# else:
#     print("Please provide valid operators " + operator)


# for i in range(1, 20):
#     if i % 2 != 0:
#         print(" this number is odd :", i)
#
# money_invester = input("enter amount for investment: ")
# interest_rate = input("enter interest rate: ")
#
# money_invester = float(money_invester)
# interest_rate = float(interest_rate) * .01
#
# for i in range(10):
#     money_invester = money_invester + (money_invester * interest_rate)
# print("Amount after 10 years is: {:.2f} ".format(money_invester))

height = input("enter the height of tree: ")
height = int(height)

spaces = height - 1
hashesh = 1
stump_spaces = height -1

while(height != 0):
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashesh):
        print('$', end="")
    print()
    spaces -= 1
    hashesh += 2
    height -= 1
for i in range(stump_spaces):
    print(' ', end="")
print('$', end="")















