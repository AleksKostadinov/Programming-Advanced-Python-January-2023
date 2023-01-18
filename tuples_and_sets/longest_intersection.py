number_ranges = int(input())
longest_intersection = set()

for i in range(number_ranges):
    first_data, second_data = input().split('-')
    first_data = first_data.split(',')
    second_data = second_data.split(',')

    first_range = set(range(int(first_data[0]), int(first_data[-1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[-1]) + 1))

    intersec = first_range.intersection(second_range)

    if len(longest_intersection) < len(intersec):
        longest_intersection = intersec

print(f"Longest intersection is {sorted(longest_intersection)}"
      f" with length {len(longest_intersection)}")
