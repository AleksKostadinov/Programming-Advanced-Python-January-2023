def students_credits(*args):
    current_course = {}
    for arg in args:
        course, credit, max_points, diyans_points = [int(x) if x.isdigit() else x for x in arg.split('-')]
        current_credits = credit * (diyans_points / max_points)
        current_course[course] = current_credits

    total_credits = sum(current_course.values())

    if total_credits >= 240:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n"

    for key, value in sorted(current_course.items(), key=lambda x: (-x[1])):
        result += f'{key} - {value:.1f}\n'
    return result

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)