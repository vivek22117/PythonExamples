shopping_list = ["banana", "orange", "pears"]

stock = {
    "banana": 6,
    "orange": 30,
    "apple": 0,
    "pears": 10,
    "disk": 55
}

prices = {
    "banana": 10,
    "orange": 12,
    "disk": 25,
    "apple": 11,
    "pears": 2
}
# compute method is below


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = prices[item] + total
            stock[item] -= 1

    return print(total)


compute_bill(shopping_list)
