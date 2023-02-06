def shopping_cart(*args):
    result_dict = {'Pizza': [], 'Soup': [], 'Dessert': []}
    result = ''
    limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    empty_cart = True
    for command  in args:
        if command  == 'Stop':
            break
        meals, products = command
        if meals not in result_dict:
            result_dict[meals] = []
        if len(result_dict[meals]) != limit[meals]:
            if products not in result_dict[meals]:
                result_dict[meals].append(products)
                empty_cart = False

    if empty_cart:
        return f'No products in the cart!'
    else:
        for key, value in sorted(result_dict.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f'{key}:\n'
            for product in sorted(value):
                result += f' - {product}\n'
        return result

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

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))








