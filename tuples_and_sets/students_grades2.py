number_students = int(input())
students_dict = {}

for _ in range(number_students):
    name, grade = input().split()
    students_dict[name] = students_dict.get(name, [])
    students_dict[name].append(f"{float(grade):.2f}")

for students, grades in students_dict.items():
    print(f"{students} -> {' '.join(grades)} (avg: {(sum(float(num) for num in grades)/len(grades)):.2f})")
