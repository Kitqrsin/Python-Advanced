from collections import deque
queue_of_customers = deque([])
number_of_customers = 0
# optimization:
# instead of creating another variable for counting the number of customers on the queue
# print out len(queue_of_customers) and it will give out the exact number of customers left
while True:
    user_input = input()
    if user_input == "Paid":
        for i in range(len(queue_of_customers)):
            number_of_customers -= 1
            print(queue_of_customers.popleft())
    elif user_input == "End":
        print(f'{number_of_customers} people remaining.')
        break
    else:
        number_of_customers += 1
        queue_of_customers.append(user_input)
