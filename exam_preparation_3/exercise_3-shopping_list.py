def shopping_list(budget, **kwargs):
    function_result = ''
    types_of_product = set()
    if budget < 100:
        return 'You do not have enough budget.'

    for current_product, values in kwargs.items():
        price, quantity = values
        if len(types_of_product) > 4:
            break
        if budget >= price*quantity:
            types_of_product.add(current_product)
            budget -= price*quantity
            function_result += f'You bought {current_product} for {price*quantity:.2f} leva.\n'

    return function_result

