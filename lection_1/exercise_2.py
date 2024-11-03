mathematics_expression = list(input())
parenthesis_start = []
for i in range(len(mathematics_expression)):
    if mathematics_expression[i] == '(':
        parenthesis_start.append(i)
    if mathematics_expression[i] == ')':
        print(''.join(mathematics_expression[parenthesis_start.pop():i+1]))
#                           ^^^ MY SOLUTION ^^^
