# box_of_clothes = input().split()
# capacity_rack = int(input())
# summed_value = 0
# used_racks = 1
#
# for i in range(len(box_of_clothes)):
#     current_value = int(box_of_clothes.pop())
#     summed_value += current_value
#
# while summed_value >= capacity_rack:
#     summed_value -= capacity_rack
#     used_racks += 1
#
# if summed_value != 0:
#     used_racks += 1
#
# print(used_racks)
clothes = [int(x) for x in input().split()]
rack_space = int(input())
racks_count = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = rack_space - cloth

print(racks_count)







