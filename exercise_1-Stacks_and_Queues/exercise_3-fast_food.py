import sys
from collections import deque
quantity_food = int(input())

orders_pending = deque(input().split())
biggest_order = -sys.maxsize

for i in range(len(orders_pending)):
    current_order = int(orders_pending[i])
    if current_order > biggest_order:
        biggest_order = current_order
while len(orders_pending) > 0:
    current_order = int(orders_pending.popleft())
    if quantity_food < current_order:
        orders_pending.appendleft(f'{current_order}')
        print(f'{biggest_order}\n'
              f'Orders left: {" ".join(orders_pending)}')
        break
    else:
        quantity_food -= current_order
if len(orders_pending) == 0:
    print(f'{biggest_order}\n'
          f'Orders complete')
