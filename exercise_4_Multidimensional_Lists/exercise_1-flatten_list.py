from collections import deque
flatten_list = [[int(x) for x in el.split() if x != ' '] for el in input().split("|")]

reversed_list = deque([])
for row in flatten_list:
    if not row:
        continue
    reversed_list.appendleft(row)

for row in reversed_list:
    print(*row, end=' ')