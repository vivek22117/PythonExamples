students = ['vivek', 'varun', 'arti', 'harsha', 'varsha', 'prashant',
            'sunil', 'somnath', 'vijay', 'manish']

good_stud = []
for stud in students:
    if stud.startswith('v'):
        good_stud.append(stud)

# print(good_stud)


# By using List Comprehension

good_stud = [stud for stud in students if stud.startswith('v')]
print(good_stud)


square_numbers = [x**2 for x in range(1, 101)]

print(square_numbers)
