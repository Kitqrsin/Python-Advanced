def kwargs_length(**kwargs):
    length = 0
    for element in kwargs.items():
        length += 1
    return length
