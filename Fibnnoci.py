def fibnocci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        result = fibnocci(number - 1) + fibnocci(number - 2)
        return result


print(fibnocci(8))

# num_values = int(input("How many fib values do you want: "))
#
# i = 1
# while i > num_values:
#     fib_value = fibnocci(i)
#     print(fib_value)
#
#     i += 1
#
# print("All done")
