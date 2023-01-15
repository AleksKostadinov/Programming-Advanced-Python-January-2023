number_students = int(input())
students_dict = {}

for _ in range(number_students):
    name, grade = input().split()
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for students, grades in students_dict.items():
    converted_value = ' '.join(map(lambda x: f"{x:.2f}", grades))
    average_grade = sum(grades) / len(grades)
    print(f'{students} -> {converted_value} (avg: {average_grade:.2f})')
