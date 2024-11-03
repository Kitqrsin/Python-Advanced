parentheses = input()

opened_list = ['{', '[', '(']
closed_list = ['}', ']', ')']


def check(user_input):
    stack = []
    for i in user_input:
        if i in opened_list:
            stack.append(i)
        elif i in closed_list:
            test = closed_list.index(i)
            if ((len(stack) > 0) and
                (opened_list[test] == stack.pop())):
                 pass
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


print(check(parentheses))
