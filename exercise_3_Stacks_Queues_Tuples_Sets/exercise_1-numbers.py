from collections import deque
first_int_sequence = set(int(x) for x in input().split())
second_int_sequence = set(int(x) for x in input().split())


def add_remove(current_command, sequence_one, sequence_two, numbers):
    if current_command == 'Add First':
        for i in numbers:
            sequence_one.add(i)

    elif current_command == 'Add Second':
        for i in numbers:
            sequence_two.add(i)

    elif current_command == 'Remove First':
        for i in numbers:
            sequence_one.discard(i)

    elif current_command == 'Remove Second':
        for i in numbers:
            sequence_two.discard(i)


for _ in range(int(input())):
    user_input = deque(input().split())
    user_command = user_input.popleft() + ' ' + user_input.popleft()
    integers = [int(x) for x in user_input]
    if user_command == 'Check Subset':
        if first_int_sequence.issubset(second_int_sequence) or second_int_sequence.issubset(first_int_sequence):
            print('True')
        else:
            print('False')
    else:
        add_remove(user_command, first_int_sequence, second_int_sequence, integers)

print(*sorted(first_int_sequence), sep=', ')
print(*sorted(second_int_sequence), sep=', ')

