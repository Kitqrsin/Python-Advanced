values_odd = set()
values_even = set()


for i in range(int(input())):
    divider = i + 1
    current_sum = 0

    for letter in input():
        current_sum += ord(letter)

    current_sum //= divider

    if current_sum % 2 == 0:
        values_even.add(current_sum)
    else:
        values_odd.add(current_sum)

sum_of_values_odd = sum(values_odd)
sum_of_values_even = sum(values_even)

if sum_of_values_odd == sum_of_values_even:
    print(*values_odd.union(values_even), sep=', ')

elif sum_of_values_odd > sum_of_values_even:
    print(*values_odd.difference(values_even), sep=', ')

elif sum_of_values_odd < sum_of_values_even:
    print(*values_even.symmetric_difference(values_odd), sep=', ')
