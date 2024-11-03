from collections import deque
evaluation = deque(input().split())


current_numbers = deque()
for number in evaluation:

    if number == "*":
        equation = 1

        if current_numbers:
            for _ in range(len(current_numbers)):
                current_number = current_numbers.popleft()
                equation *= current_number

        current_numbers.appendleft(equation)

    elif number == "+":
        equation = 0

        if current_numbers:
            for _ in range(len(current_numbers)):
                current_number = current_numbers.popleft()
                equation += current_number

            current_numbers.appendleft(equation)

    elif number == "-":

        if current_numbers:
            equation = current_numbers.popleft()
            for _ in range(len(current_numbers)):
                current_number = current_numbers.popleft()
                equation -= current_number

            current_numbers.appendleft(equation)

    elif number == "/":

        if current_numbers:
            equation = current_numbers.popleft()
            for _ in range(len(current_numbers)):
                current_number = current_numbers.popleft()
                equation = equation // current_number

            current_numbers.appendleft(equation)

    else:
        current_numbers.append(int(number))

print(*current_numbers)
