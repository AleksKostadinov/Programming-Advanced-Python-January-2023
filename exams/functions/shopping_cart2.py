def shopping_cart(*args):
    meal_dict = {
        'Pizza': [],
        'Soup': [],
        'Dessert': [],
    }
    limit_dict = {
        'Pizza': 4,
        'Soup': 3,
        'Dessert': 2,
    }
    result = []
    empty_cart = True

    for arg in args:
        if arg == 'Stop':
            break
        meal, product = arg
        if len(meal_dict[meal]) != limit_dict[meal]:
            if not product in meal_dict[meal]:
                meal_dict[meal].append(product)
                empty_cart = False

    for meals, products in sorted(meal_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f'{meals}:')
        for value in sorted(products):
            result.append(f' - {value}')
    if empty_cart:
        return 'No products in the cart!'
    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))



