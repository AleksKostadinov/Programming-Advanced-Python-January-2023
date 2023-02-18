def shop_from_grocery_list(budget, grocery_list, *products):
    purchased = set()

    for name, price in products:
        if name in grocery_list and name not in purchased:
            if price > budget:
                break
            budget -= price
            purchased.add(name)

    if len(grocery_list) == len(purchased):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = sorted(set(grocery_list) - purchased)
        return f"You did not buy all the products. Missing products: {', '.join(map(str, missing_products))}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
