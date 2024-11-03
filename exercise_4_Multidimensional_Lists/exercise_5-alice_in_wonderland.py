size = int(input())

matrix = []
alice_pos = []

for row in range(size):  # read the matrix and find Alice's position
    matrix.append(input().split())
    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '*'  # mark Alice's position as already discovered

collected_tea_bags = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while collected_tea_bags < 10:
    user_command = input()
    row, col = [
        alice_pos[0] + directions[user_command][0],
        alice_pos[1] + directions[user_command][1]
    ]

    if not (size > row >= 0 and size > col >= 0):
        break

    current_position = matrix[row][col]
    alice_pos = [row, col]
    matrix[row][col] = '*'
    if current_position == 'R':
        break
    if current_position.isdigit():
        collected_tea_bags += int(current_position)

if collected_tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*el) for el in matrix]
