# find factorial of a given number
def factorial_example(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial_example(num - 1)
        return result

print(factorial_example(4))

