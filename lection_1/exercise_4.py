from collections import deque
water_quantity = int(input())
people = deque()
while True:
    new_person = input()
    if new_person == 'Start':
        break
    people.append(new_person)

command_given = input()

while command_given != "End":
    data = command_given.split()
    if data[0] == 'refill':
        refill = int(data[1])
        water_quantity += refill
    else:
        current_person = people.popleft()
        water_used = int(data[0])
        if water_quantity < water_used:
            print(f'{current_person} must wait')
        else:
            print(f'{current_person} got water')
            water_quantity -= water_used
    command_given = input()

print(f'{water_quantity} liters left')
