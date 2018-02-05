# find factorial of a given number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print("Enter the value for factorial: ")

num = int(input())
print(factorial(num))
