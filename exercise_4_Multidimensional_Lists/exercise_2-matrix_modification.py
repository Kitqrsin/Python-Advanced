def coordinate_validation(row, col):
    if len(matrix) - 1 >= row >= 0 and len(matrix[0]) - 1 >= col >= 0:
        return True


def subtraction(row, col, value):
    if coordinate_validation(row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")


def addition(row, col, value):
    if coordinate_validation(row, col):
        matrix[row][col] += value
    else:
        print("Invalid coordinates")


rows = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
user_input = input().split()

while user_input[0] != 'END':

    command = user_input[0]
    if len(user_input) == 4:
        current_row, current_col, current_value = [int(el) for el in user_input[1:4]]
    else:
        print("Invalid coordinates")
        continue

    if command == 'Add':
        addition(current_row, current_col, current_value)

    elif command == 'Subtract':
        subtraction(current_row, current_col, current_value)

    user_input = input().split()

for row in matrix:
    print(*row)