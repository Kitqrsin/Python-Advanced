def rover_movement(movement_dict, current_position, command):
    new_position = [
        current_position[0] + movement_dict[command][0],
        current_position[1] + movement_dict[command][1]
    ]
    if 0 <= new_position[0] < MATRIX_SIZE and 0 <= new_position[1] < MATRIX_SIZE:
        return new_position
#   rover is in the matrix

    if new_position[0] >= MATRIX_SIZE:
        new_position[0] = 0
#   rover moves out of the matrix downside

    if new_position[0] < 0:
        new_position[0] = MATRIX_SIZE - 1
#   rover moves out of the matrix upside

    if new_position[1] >= MATRIX_SIZE:
        new_position[1] = 0
#   rover moves out of the matrix right side

    if new_position[1] < 0:
        new_position[1] = MATRIX_SIZE - 1
#   rover moves out of the matrix left side

    return new_position


MATRIX_SIZE = 6
matrix = []
rover_pos = [0, 0]

for current_row in range(MATRIX_SIZE):
    sub_matrix = [el for el in input().split()]
    if 'E' in sub_matrix:
        rover_pos = [current_row, sub_matrix.index('E')]
    matrix.append(sub_matrix)
# reading the matrix

MOVEMENT = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}


water_deposit_found = False
metal_deposit_found = False
concrete_deposit_found = False


user_commands = input().split(', ')

for current_command in user_commands:
    matrix[rover_pos[0]][rover_pos[1]] = '-'
    rover_pos = rover_movement(MOVEMENT, rover_pos, current_command)
    current_landmass = matrix[rover_pos[0]][rover_pos[1]]

    if current_landmass == 'W':
        if not water_deposit_found:
            water_deposit_found = True
        print(f'Water deposit found at ({rover_pos[0]}, {rover_pos[1]})')

    elif current_landmass == 'M':
        if not metal_deposit_found:
            metal_deposit_found = True
        print(f'Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})')

    elif current_landmass == 'C':
        if not concrete_deposit_found:
            concrete_deposit_found = True
        print(f'Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})')

    elif current_landmass == 'R':
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if water_deposit_found and metal_deposit_found and concrete_deposit_found:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
