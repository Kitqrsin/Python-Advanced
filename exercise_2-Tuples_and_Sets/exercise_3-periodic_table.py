set_of_elements = set()

for _ in range(int(input())):
    chemical_element = input().split()
    for i in chemical_element:
        set_of_elements.add(i)

print(*set_of_elements, sep='\n')


# periodic_table = set(element for element in (input().split() for i in range(int(input()))))
# print(*periodic_table)
