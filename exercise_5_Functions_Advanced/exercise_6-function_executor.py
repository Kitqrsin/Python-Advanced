def func_executor(*args):
    result = ''
    for name, parameters in args:
        function = name.__name__
        result += f'{function} - {name(*parameters)}\n'
    return result
