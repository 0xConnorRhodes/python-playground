menu = {
        'hamburger': 10,
        'taco': 5,
        'salad': 8
        }

orders = []
total_cost = 0
while True:
    order = input('What do you want to order?\n').strip().lower()

    if order == '':
        break
    elif order not in menu:
        print("Sorry that's not on the menu.")
        continue
    else:
        orders.append(order.capitalize())
        total_cost += menu[order]

print('You ordered:' + '\n' + '\n'.join(orders) + '\n\n' + 'for a total cost of: $' + str(total_cost))


