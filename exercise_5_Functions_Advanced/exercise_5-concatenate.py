def concatenate(*args, **kwargs):
    concatenation = ''
    for letter in args:
        concatenation += letter
    for key, value in kwargs.items():
        if key in concatenation:
            concatenation = concatenation.replace(key, value)
    return concatenation

