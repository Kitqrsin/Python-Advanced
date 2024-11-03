unique_names = set()
for _ in range(int(input())):
    current_name = input()
    unique_names.add(current_name)

for name in unique_names:
    print(name)
# print(*names, sep='\n')
