#                                       string = input()
#                                       stack = []
#                                       length_of_string = 0
#                                       for i in string:
#                                           stack.append(i)
#                                           length_of_string +=1
#                                       stack_reverse = []
#                                       for i in range(length_of_string):
#                                           element = stack.pop()
#                                           stack_reverse.append(element)
#                                       print(''.join(stack_reverse))
#                           ^^^ MY SOLUTION ^^^

# correction to my code,
# instead of counting how many actions have been taken in the first for loop
# you can make string into a list by using list(input()) and then you can use len(string) in the
# for loop

# the more optimized version of my code:
#                                       string = list(input())
#                                       stack = []
#                                       for i in range(len(string)):
#                                           stack.append(string.pop())
#                                       print(''.join(stack))


string = list(input())
while string:
    print(string.pop(), end='')