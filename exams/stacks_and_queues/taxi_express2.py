from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = deque(int(x) for x in input().split(', '))

total_time = 0

while customers and taxis:
    first_customer = customers.popleft()
    last_taxi = taxis.pop()

    if first_customer <= last_taxi:
        total_time += first_customer
    else:
        customers.appendleft(first_customer)

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str, customers))}')
