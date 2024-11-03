user_input = input()
table = sorted([x for x in user_input])
table_set = set()

for element in table:
    if element in table_set:
        continue
    else:
        print(f'{element}: {table.count(element)} time/s')
        table_set.add(element)




