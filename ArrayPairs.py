'''
Pair the array values which are sum of provided answer.

example: ([1,2,2,3], 4) gives output as (2,2) and (1,3)
'''


def pair_nums(array, n):
    if len(array) < 2:
        return print("The size of array is too small")

    seen = set()
    output = set()

    for num in array:
        target = n - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

pair_nums([1, 2, 2, 3], 4)
