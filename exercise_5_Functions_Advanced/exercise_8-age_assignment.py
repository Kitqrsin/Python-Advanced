def age_assignment(*args, **kwargs):
    names_list = {}
    for first_letter, age in kwargs.items():
        for word in args:
            if first_letter in word:
                names_list[word] = age
    result = ''
    for name, age in dict(sorted(names_list.items(), key=lambda kvp: kvp[0])).items():
        result += f"{name} is {age} years old.\n"
    return result
