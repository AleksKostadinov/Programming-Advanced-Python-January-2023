from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque([int(x) for x in input().split()])
reward = int(input())

barrel_count, shoot_count = 0, 0

while bullets and locks:
    bullet = bullets.pop()
    barrel_count += 1
    shoot_count += 1
    current_lock = locks[0]

    if bullet <= current_lock:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')
    if barrel_count == size_barrel and bullets:
        barrel_count = 0
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = reward - shoot_count * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
