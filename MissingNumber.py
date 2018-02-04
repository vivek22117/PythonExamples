'''
find missing number in second array as comapred to first array
'''


def finder(array1, array2):

    array1.sort()
    array2.sort()

    for num1, num2 in zip(array1, array2):
        if num1 != num2:
            return num1

    return array1[-1]

print(finder([1, 2, 3, 4, 5, 6, 7], [1, 3, 6, 2, 5, 4]))
