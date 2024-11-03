from collections import deque
worker_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
honey_accumulated = 0


def accumulation(symbol, worker, nectar):
    if symbol == '+':
        return abs(worker + nectar)

    elif symbol == '-':
        return abs(worker - nectar)

    elif symbol == '*':
        return abs(worker * nectar)

    elif symbol == '/':
        if nectar == 0:
            return 0
        else:
            return abs(worker / nectar)


while worker_bees and nectar:
    current_worker = worker_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_worker:
        current_symbol = symbols.popleft()
        honey_accumulated += accumulation(current_symbol, current_worker, current_nectar)
    else:
        while nectar:
            current_nectar = nectar.pop()
            if current_worker > current_nectar:
                continue
            else:
                current_symbol = symbols.popleft()
                honey_accumulated += accumulation(current_symbol, current_worker, current_nectar)
                break


print(f'Total honey made: {honey_accumulated}')

if worker_bees:
    print(f'Bees left: {", ".join([f"{x}" for x in worker_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([f"{x}" for x in nectar])}')
