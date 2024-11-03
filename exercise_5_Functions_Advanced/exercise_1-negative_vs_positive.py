def negative_vs_positive(*args):
    sum_of_negatives = 0
    sum_of_positives = 0
    for element in range(len(args[0])):
        if args[0][element] < 0:
            sum_of_negatives += args[0][element]
        else:
            sum_of_positives += args[0][element]
    print(sum_of_negatives)
    print(sum_of_positives)
    if abs(sum_of_negatives) > sum_of_positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


user_input = [int(el) for el in input().split()]
negative_vs_positive(user_input)