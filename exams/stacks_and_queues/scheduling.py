jobs = [int(x) for x in input().split(", ")]
searched_index = int(input())
cycles = 0


def change_number(index):
    jobs[index] = "x"


for num in sorted(jobs):
    found_index = jobs.index(num)
    cycles += jobs[found_index]
    change_number(found_index)
    if found_index == searched_index:
        break

print(cycles)
