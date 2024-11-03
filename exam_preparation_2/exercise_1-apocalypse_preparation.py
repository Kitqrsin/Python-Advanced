from collections import deque

textiles = deque([int(el) for el in input().split()])
meds = [int(el) for el in input().split()]

ITEMS = {
    'MedKit': 0,
    'Bandage': 0,
    'Patch': 0,
}


while len(textiles) > 0 and len(meds) > 0:
    first_textile = textiles.popleft()
    last_med = meds.pop()
    total_sum = first_textile + last_med

    if total_sum == 30:
        ITEMS['Patch'] += 1

    elif total_sum == 40:
        ITEMS['Bandage'] += 1

    elif total_sum == 100:
        ITEMS['MedKit'] += 1

    elif total_sum > 100:
        meds[len(meds) - 1] += total_sum - 100
        ITEMS['MedKit'] += 1

    else:
        last_med += 10
        meds.append(last_med)

sorted_items_dict = sorted(ITEMS.items(), key=lambda kvp: (-kvp[1], kvp[0]))

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
    for item, value in sorted_items_dict:
        if value > 0:
            print(f'{item} - {value}')

elif textiles:
    print("Medicaments are empty.")
    for item, value in sorted_items_dict:
        if value > 0:
            print(f'{item} - {value}')
    print(f'Textiles left: {", ".join([str(el) for el in textiles])}')

elif meds:
    print("Textiles are empty.")
    for item, value in sorted_items_dict:
        if value > 0:
            print(f'{item} - {value}')
    print(f'Medicaments left: {", ".join([str(el) for el in sorted(meds, reverse=True)])}')

