from collections import deque
chocolates = deque([int(x) for x in input().split(', ')])
cups_of_milk = deque([int(x) for x in input().split(', ')])


prepared_milkshakes = 0

while prepared_milkshakes < 5 and (len(chocolates) > 0 and len(cups_of_milk) > 0):
    current_chocolate = chocolates.pop()
    current_cup = cups_of_milk.popleft()
    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    if current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_cup == current_chocolate:
        prepared_milkshakes += 1

    else:
        cups_of_milk.append(current_cup)
        current_chocolate -= 5
        if current_chocolate >= 0:
            chocolates.append(current_chocolate)

if prepared_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([f'{x}' for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([f'{x}' for x in cups_of_milk])}")
else:
    print("Milk: empty")
