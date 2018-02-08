pets = ['dog', 'cat', 'horse', 'mouse', 'parrot', 'pig']

print(pets[1])
print(pets[3])
print(pets[2])
print(pets[4], '\n')

for values in pets:
    print(values)

got_rupees = 100

while got_rupees < 110:
    print(got_rupees)
    got_rupees += 1

print("I need more money", '\n')

for i in range(2000, 2050):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

import random

target_number, guess_number = random.randint(1, 15), 0
while target_number != guess_number:
    guess_number = int(input("Enter the guess number to win the game"))

print("Won!")

count = 0
for num in range(7):
    count += 1
    print("*" * count)
for num in range(6):
    count -= 1
    print("*" * count)
