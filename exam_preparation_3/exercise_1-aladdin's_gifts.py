from collections import deque


def gift_creation(elements):

    if 100 <= elements <= 199:
        gifts_made['Gemstone'] += 1
        return True

    elif 200 <= elements <= 299:
        gifts_made['Porcelain Sculpture'] += 1
        return True

    elif 300 <= elements <= 399:
        gifts_made['Gold'] += 1
        return True

    elif 400 <= elements <= 499:
        gifts_made['Diamond Jewellery'] += 1
        return True

    else:
        return False


materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])

gifts_made = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}


while len(materials) > 0 and len(magic) > 0:
    last_material = materials.pop()
    first_magic = magic.popleft()
    sum_of_elements = last_material + first_magic

    while sum_of_elements < 100:
        if sum_of_elements % 2 == 0:
            last_material *= 2
            first_magic *= 3
            sum_of_elements = last_material + first_magic
            break
        else:
            sum_of_elements *= 2

    if gift_creation(sum_of_elements):
        pass
    else:
        gift_creation(sum_of_elements / 2)


if (gifts_made['Gold'] > 0 and gifts_made['Diamond Jewellery'] > 0) or\
    (gifts_made['Gemstone'] > 0 and gifts_made['Porcelain Sculpture'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if magic:
    print(f'Magic left: {", ".join([str(el) for el in magic])}')
elif materials:
    print(f'Materials left: {", ".join([str(el) for el in materials])}')


sorted_dict = sorted(gifts_made.items(), key=lambda kvp: kvp[0])
for gift, quantity in sorted_dict:
    if quantity > 0:
        print(f'{gift}: {quantity}')
