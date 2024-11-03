from collections import deque
#                               kids = deque(input().split())
#                               tosses = int(input())
#                               tosses_used = 0
#                               while len(kids) > 1:
#                                   current_kid = kids.popleft()
#                                   if tosses_used == tosses - 1:
#                                       print(f'Removed {current_kid}')
#                                       tosses_used = 0
#                                   else:
#                                       tosses_used += 1
#                                       kids.append(current_kid)
#
#                               print(f'Last is {"".join(kids)}')

#                                     ^^^ MY SOLUTION ^^^
kids = deque(input().split())
tosses = int(input()) - 1
while len(kids) > 1:
    kids.rotate(-tosses)
    current_kid = kids.popleft()
    print(f'Removed {current_kid}')
print(f'Last is {"".join(kids)}')