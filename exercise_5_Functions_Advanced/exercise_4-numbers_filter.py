def even_odd_filter(**kwargs):

    def even_numbers(*args):
        result = []
        for num in args[0]:
            if num % 2 == 0:
                result.append(num)
        return result

    def odd_numbers(*args):
        result = []
        for num in args[0]:
            if num % 2 != 0:
                result.append(num)
        return result

    num_dict = {}
    for command, nums in kwargs.items():
        if command == 'even':
            num_dict[command] = even_numbers(nums)
        elif command == "odd":
            num_dict[command] = odd_numbers(nums)
    sorted_dict = sorted(num_dict.items(), key=lambda x: -len(x[1]))
    return {el: key for el, key in sorted_dict}

