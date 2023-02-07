from collections import deque

orders = deque(int(x) for x in input().split(', '))
employees = deque(int(x) for x in input().split(', '))
total_pizzas = 0

while orders and employees:
    first_order = orders.popleft()
    if first_order > 10 or first_order <= 0:
        continue
    last_employees = employees.pop()
    if first_order <= last_employees:
        total_pizzas += first_order
    else:
        first_order -= last_employees
        total_pizzas += last_employees
        orders.appendleft(first_order)

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}\nEmployees: {", ".join(map(str, employees))}')

else:
    print(f'Not all orders are completed.\nOrders left: {", ".join(map(str, orders))}')
