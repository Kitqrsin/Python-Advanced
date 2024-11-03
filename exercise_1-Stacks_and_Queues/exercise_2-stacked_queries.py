import sys

stack = []
integer = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
for _ in range(integer):
    query = input().split()
    command = int(query[0])

    if command == 1:
        expression = int(query[1])
        stack.append(expression)
    elif command == 2:
        if len(stack) <= 0:
            continue
        else:
            stack.pop()
    elif command == 3:
        if len(stack) <= 0:
            continue
        for element in range(len(stack)):
            current_number = stack[element]
            if current_number > max_number:
                max_number = current_number
            else:
                continue
        print(max_number)
        max_number = -sys.maxsize
    elif command == 4:
        if len(stack) <= 0:
            continue
        for element in range(len(stack)):
            current_number = stack[element]
            if current_number < min_number:
                min_number = current_number
            else:
                continue
        print(min_number)
        min_number = sys.maxsize

final_stack = []
for i in range(len(stack)):
    final_stack.append(f'{stack.pop()}')
print(', '.join(final_stack))






