from collections import deque

portions = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}
not_conquered = 5
conquered = []
days = 0

while peaks and portions and stamina:
    energy = portions.pop() + stamina.popleft()

    for peak, diff in peaks.items():
        if energy >= diff:
            conquered.append(peak)
            del peaks[peak]
            not_conquered -= 1
            break
        else:
            break
    days += 1

    if days == 7:
        break

if not_conquered:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conquered:
    print('Conquered peaks:')
    print(*conquered, sep="\n")
