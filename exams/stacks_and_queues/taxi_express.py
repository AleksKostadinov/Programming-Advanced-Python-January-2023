from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = deque(int(x) for x in input().split(', '))

total_time = 0

while customers and taxis:

    if customers[0] <= taxis[-1]:
        first_customer = customers.popleft()
        last_taxi = taxis.pop()
        total_time += first_customer
    else:
        last_taxi = taxis.pop()

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str, customers))}')
