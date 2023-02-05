def calculate_func(course_, credit_, max_points_, diyans_points_):
    current_course = {}
    current_credits = credit_ * (diyans_points_ / max_points_)
    if not course_ in current_course:
        current_course[course_] = current_credits
    return current_course

def students_credits(*args):
    total_credits = 0
    total_courses = {}
    for arg in args:
        course, credit, max_points, diyans_points = [int(x) if x.isdigit() else x for x in arg.split('-')]
        current_course = calculate_func(course, credit, max_points, diyans_points)

        for key, value in current_course.items():
            total_credits += value
            if not key in total_courses:
                total_courses[key] = value


    credits_needed = 240
    if total_credits >= 240:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {(credits_needed - total_credits):.1f} credits more for a diploma.\n"

    for key, value in sorted(total_courses.items(), key=lambda x: (-x[1])):
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



