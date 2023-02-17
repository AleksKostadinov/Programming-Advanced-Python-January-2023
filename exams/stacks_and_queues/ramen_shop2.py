from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:
    value_ramen = bowls_of_ramen[-1]
    value_customers = customers[0]

    if value_ramen == value_customers:
        bowls_of_ramen.pop()
        customers.popleft()
    elif value_ramen > value_customers:
        bowls_of_ramen[-1] -= value_customers
        customers.popleft()
    elif value_ramen < value_customers:
        customers[0] -= value_ramen
        bowls_of_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls_of_ramen))}')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(map(str, customers))}')
