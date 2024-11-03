def even_odd(*args):
    numbers = []
    if args[-1] == 'even':
        for element in args[0:-1]:
            if element % 2 == 0:
                numbers.append(element)
        return numbers
    elif args[-1] == 'odd':
        for element in args[0:-1]:
            if element % 2 != 0:
                numbers.append(element)
        return numbers
