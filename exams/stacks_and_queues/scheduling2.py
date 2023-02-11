jobs = [int(x) for x in input().split(", ")]
searched_index = int(input())

cycles = 0
job = jobs[searched_index]

while job in jobs:
    cycles += min(jobs)
    jobs.remove(min(jobs))

print(cycles)
