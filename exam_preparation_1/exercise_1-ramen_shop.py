from collections import deque
bowls_of_ramen = [int(el) for el in input().split(', ')]
customers = deque([int(el) for el in input().split(', ')])

while len(bowls_of_ramen) > 0 and len(customers) > 0:
    last_bowl = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if last_bowl == first_customer:
        continue

    elif last_bowl > first_customer:
        last_bowl -= first_customer
        if last_bowl > 0:
            bowls_of_ramen.append(last_bowl)

    else:
        first_customer -= last_bowl
        if first_customer > 0:
            customers.appendleft(first_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(el) for el in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
