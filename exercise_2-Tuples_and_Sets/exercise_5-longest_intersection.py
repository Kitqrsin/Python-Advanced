import sys

ranges_dict = {}

longest_intersection = []
longest_intersection_length = -sys.maxsize


for i in range(int(input())):
    user_set_ranges = [[int(x) for x in x.split(",")] for x in input().split('-')] #[[0, 3], [1, 2]]
    ranges_dict[i] = set(range(user_set_ranges[0][0], user_set_ranges[0][1] + 1)),\
                     set(range(user_set_ranges[1][0], user_set_ranges[1][1] + 1))
                    #first_dictionary: first_set(0, 1, 2, 3), second_set(1, 2)


for element, sets in ranges_dict.items():
    current_intersection = sets[0].intersection(sets[1])
    if len(current_intersection) > longest_intersection_length:
        longest_intersection_length = len(current_intersection)
        longest_intersection = [f'{x}' for x in current_intersection]


print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {longest_intersection_length}')
