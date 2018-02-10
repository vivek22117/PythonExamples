customers = []

while True:
    check_entry = input("Enter new customer: ")
    check_entry = check_entry[0].lower()
    if check_entry == 'n':
        break
    else:
        fName, lName = input("Enter customer Name: ").split(' ')
        customers.append({'fName':fName, 'lName': lName})

for cus in customers:
    print(cus['fName'], cus['lName'])
