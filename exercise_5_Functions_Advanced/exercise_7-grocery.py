def grocery_store(**kwargs):
    lists_of_products = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = ''
    for product, quantity in lists_of_products.items():
        result += f'{product}: {quantity}\n'
    return result
