from collections import deque

food_portion = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

conquered_peaks = []
energy = 0
day = 1

peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}

while peaks and food_portion and stamina:
        if day > 7:
            break

        energy = food_portion.pop() + stamina.popleft()
        for peak in peaks.copy():
            if energy >= peaks[peak]:
                energy -= peaks[peak]
                conquered_peaks.append(peak)
                del peaks[peak]
            else:
                day += 1
                break

if not peaks:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    print('\n'.join(conquered_peaks))