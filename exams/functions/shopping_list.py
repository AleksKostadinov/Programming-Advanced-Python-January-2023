def shopping_list(budget, **keywords):
    products = []
    result = ''
    if budget < 100:
        return f'You do not have enough budget.'

    for product, value in keywords.items():
    # for product, (price, quantity) in keywords.items():
        price, quantity = value
        current_price = price * quantity
        if budget >= current_price:
            products.append(product)
            budget -= current_price
            result += f'You bought {product} for {current_price:.2f} leva.\n'

        if len(products) == 5:
            return result

    return result

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
