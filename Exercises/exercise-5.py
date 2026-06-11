
# =====================================================
# Exercise 5: University Course Registration System
# =====================================================

courses = [
    ("Math", 45),
    ("Physics", 60),
    ("Biology", 25),
    ("Chemistry", 75),
    ("History", 30)
]


def highest_enrollment(course_list):
    """
    Return course with highest enrollment.
    """
    return max(enrollment for subject, enrollment in course_list)
    


def low_enrollment_courses(course_list):
    """
    Return courses with enrollment below 40.
    """
    return (e for s, e in course_list if e < 41)


def total_registered_students(course_list):
    """
    Calculate total registered students.
    """
    return sum(e for s, e in course_list)


def add_extra_students(course_list):
    """
    Add 5 extra students using map().
    """
    return list(map(lambda x: (x[0], x[1] + 1), course_list))


def sort_courses(course_list):
    """
    Sort courses by enrollment.
    """
    return sorted(course_list, key=lambda x: x[1])


def process_enrollments(course_list):
    """
    Square even enrollments.
    Cube odd enrollments.
    """
    return [e ** 2 if e % 2 == 0 else e ** 3 for s, e in course_list]


def popular_courses(course_list):
    """
    Use filter() to get courses above 50 students.
    """
    return filter(lambda x: x[1] >= 50, course_list)


print(highest_enrollment(courses))
print(list(low_enrollment_courses(courses)))
print(total_registered_students(courses))
print(add_extra_students(courses))
print(sort_courses(courses))
print(process_enrollments(courses))
print(list(popular_courses(courses)))
