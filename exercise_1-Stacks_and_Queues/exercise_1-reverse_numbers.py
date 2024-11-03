user_input = input().split()
reversed_user_input = []
for i in range(len(user_input)):
    reversed_user_input.append(user_input.pop())
print(' '.join(reversed_user_input))