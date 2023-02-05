from collections import deque

food_portion = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

conquered_peaks = []
energy = 0
day = 1

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while peaks and food_portion and stamina:
    energy = food_portion.pop() + stamina.popleft()
    peak, difficulty = peaks.popleft()
    if energy >= difficulty:
        conquered_peaks.append(peak)
        day += 1
    else:
        peaks.appendleft((peak, difficulty))
        day += 1
    if day > 7:
        break

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f"Conquered peaks:")
    print(*conquered_peaks, sep="\n")


