
def indices_validation(first_coordinate, second_coordinate,):
    if rows > first_coordinate >= 0 and rows > second_coordinate >= 0:
        return True


rows = int(input())
chess_board = [[el for el in input()] for _ in range(rows)]

knights_removed = 0
while True:
    dominant_knight = []
    dominant_knight_attacks = 0
    for row in range(rows):
        for col in range(rows):
            symbol = chess_board[row][col]
            if symbol == 'K':
                current_knight_attacks = 0
                upper_left = [row-2, col-1]
                upper_right = [row-2, col+1]
                right_up = [row - 1, col + 2]
                right_down = [row + 1, col + 2]
                left_up = [row - 1, col - 2]
                left_down = [row + 1, col - 2]
                down_left = [row + 2, col - 1]
                down_right = [row + 2, col + 1]

                if indices_validation(*upper_left):
                    if chess_board[row-2][col-1] == 'K':
                        current_knight_attacks += 1
                if indices_validation(*upper_right):
                    if chess_board[row-2][col+1] == 'K':
                        current_knight_attacks += 1

                if indices_validation(*right_up):
                    if chess_board[row-1][col+2] == 'K':
                        current_knight_attacks += 1
                if indices_validation(*right_down):
                    if chess_board[row+1][col+2] == 'K':
                        current_knight_attacks += 1

                if indices_validation(*left_up):
                    if chess_board[row-1][col-2] == 'K':
                        current_knight_attacks += 1
                if indices_validation(*left_down):
                    if chess_board[row+1][col-2] == 'K':
                        current_knight_attacks += 1

                if indices_validation(*down_left):
                    if chess_board[row+2][col-1] == 'K':
                        current_knight_attacks += 1
                if indices_validation(*down_right):
                    if chess_board[row+2][col+1] == 'K':
                        current_knight_attacks += 1

                if current_knight_attacks > dominant_knight_attacks:
                    dominant_knight = [row, col]
                    dominant_knight_attacks = current_knight_attacks
    if dominant_knight:
        chess_board[dominant_knight[0]][dominant_knight[1]] = "0"
        knights_removed += 1
    else:
        break
print(knights_removed)