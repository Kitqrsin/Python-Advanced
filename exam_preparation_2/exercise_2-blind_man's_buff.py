def blind_movement(movement_dict, current_position, current_command):
    new_position = [
        current_position[0] + movement_dict[current_command][0],
        current_position[1] + movement_dict[current_command][1]
    ]

    if 0 <= new_position[0] < ROWS and 0 <= new_position[1] < COLUMNS:
        # checking if the current position is in the matrix boundaries

        if matrix[new_position[0]][new_position[1]] == 'O':
            return current_position
        # checking if the new movement goes into an obstacle

        matrix[current_position[0]][current_position[1]] = '-'
        return new_position

    else:
        return current_position


ROWS, COLUMNS =[int(el) for el in input().split()]
matrix = []
blind_pos = [0, 0]

for current_row in range(ROWS):
    sub_matrix = input().split()
    if 'B' in sub_matrix:
        blind_pos = [current_row, sub_matrix.index('B')]
    matrix.append(sub_matrix)

MOVEMENT = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

moves_made = 0
touched_players = 0

while True:
    user_command = input()
    if user_command == 'Finish' or touched_players == 3:
        break
    blind_pos = blind_movement(MOVEMENT, blind_pos, user_command)
    current_move = matrix[blind_pos[0]][blind_pos[1]]
    if current_move == 'P':
        matrix[blind_pos[0]][blind_pos[1]] = 'B'
        touched_players += 1
        moves_made += 1

    elif current_move == '-':
        matrix[blind_pos[0]][blind_pos[1]] = 'B'
        moves_made += 1

    else:
        pass

print("Game over!\n"
      f"Touched opponents: {touched_players} Moves made: {moves_made}")


# print(blind_pos)
# [print(*el) for el in matrix]