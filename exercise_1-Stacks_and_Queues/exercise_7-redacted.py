from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(';'):
    name, time_needed = r.split('-')
    robots[name] = [int(time_needed), 0]

factory_tame = datetime.strptime(input(), '%H:%M:%S')

products = deque()

while True:
    product = input()

    if product == 'End':
        break

    products.append(product)

while products:
    factory_tame += timedelta(0, 1)
    product = products.popleft()
    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue
    robots_name, data = free_robots[0]
    robots[robots_name][1] = data[0]
    print(f'{robots_name} - {product} [{factory_tame.strftime("%H:%M:%S")}]')








