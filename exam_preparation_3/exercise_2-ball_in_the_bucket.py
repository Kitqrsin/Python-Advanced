MATRIX_SIZE = 6
matrix = []


def bucket_hit(col):
    sum_created = 0
    for current_row in range(0, 6):
        try:
            sum_created += matrix[current_row][col]
        except TypeError:
            pass
    return sum_created


for current_row in range(MATRIX_SIZE):
    sub_matrix = [int(el) if el.isdigit() else el for el in input().split()]
    # if the element given is digit it is transformed into class digit in order
    # to simplify the code further down
    matrix.append(sub_matrix)

points_accumulated = 0
for current_throw in range(3):
    given_coordinates = input()
    row_given, col_given = eval(given_coordinates)

    if 0 <= row_given < MATRIX_SIZE and 0 <= col_given < MATRIX_SIZE:

        if matrix[row_given][col_given] == 'B':
            matrix[row_given][col_given] = '-'
            points_accumulated += bucket_hit(col_given)
        #     securing that we won't hit the same bucket twice
        else:
            pass
    else:
        continue

if 100 <= points_accumulated <= 199:
    print(f"Good job! You scored {points_accumulated} points, and you've won Football.")
elif 200 <= points_accumulated <= 299:
    print(f"Good job! You scored {points_accumulated} points, and you've won Teddy Bear.")
elif 300 <= points_accumulated:
    print(f"Good job! You scored {points_accumulated} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points_accumulated} points more to win a prize.")
