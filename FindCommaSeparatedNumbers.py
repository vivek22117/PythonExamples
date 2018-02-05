# find all numbers divisible by 7 but not the multiple of 5 between 2000 to 32000

empty_list = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        empty_list.append(str(i))

print(",".join(empty_list))
