from copy import deepcopy
from collections import deque
idle_robots = deque([x for x in x.split('-')] for x in input().split(';'))
busy_robots = []
busy_robots_copy = []



def clock_management(hh, mm, ss):
    if ss >= 60:
        ss -= 60
        mm += 1
        if mm >= 60:
            mm -= 60
            hh += 1
            if hh >= 24:
                hh -= 24
                hh = 0
    return hh, mm, ss


starting_time = input().split(':')
hours = int(starting_time[0])
minutes = int(starting_time[1])
seconds = int(starting_time[2]) + 1

counter = 0
integer = 0

products_due = deque()

command = input()
while command != 'End':
    products_due.append(command)
    command = input()

while products_due:
    clock_management(hours, minutes, seconds)


    for element in busy_robots:
        time_needed = int(busy_robots_copy[integer][1])
        time_needed -= 1
        if time_needed < 1:
            idle_robots.appendleft(busy_robots.pop(integer))
            busy_robots_copy.pop(integer)
            integer += 1
        else:
            integer += 1

    if len(idle_robots) < 1:
        products_due.rotate(-1)
    else:
        hours, minutes, seconds = clock_management(hours, minutes, seconds)
        product = products_due.popleft()
        current_robot = idle_robots.popleft()
        busy_robots.append(current_robot)
        busy_robots_copy = deepcopy(busy_robots)
        name, time = current_robot
        print(f'{name} - {product} [{hours:02d}:{minutes:02d}:{seconds:02d}]')

    seconds += 1
    counter += 1
    integer = 0









