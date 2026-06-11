# =====================================================
# Exercise 1: Advanced Student Performance Analyzer
# =====================================================

from math import inf


students = [
    ("Abel", 45),
    ("Sara", 80),
    ("John", 66),
    ("Mahi", 30),
    ("Helen", 90),
    ("Ruth", 55)
]


def calculate_average(student_list):
    average_score = sum(score for name, score in student_list) /len(student_list)
    return average_score


def highest_student(student_list):
    maxi = max(score for name, score in student_list)
    return maxi


def lowest_student(student_list):
    mini = min(score for name, score in student_list)
    return mini


def passed_students(student_list):
    return [(name, score) for name, score in student_list if score >= 50]


def failed_students(student_list):
    return [(name, score) for name, score in student_list if score < 50]

def add_bonus_marks(student_list):
    return map(lambda x: (x[0], x[1] + 30) if x[0] in ["Mahi", "Abel"] else x, student_list)
    
def sort_students(student_list):
    sort_students = sorted(student_list, key=lambda x: x[1])
    return sort_students


def square_even_cube_odd(student_list):
    res = [score ** 2 if score % 2 == 0 else score ** 3 for name, score in student_list]
    return res
    


def students_above_70(student_list):
    ans = filter(lambda x: x[1] >= 70, student_list)
    return list(ans)


def assign_grades(student_list):
    """
    Assign grades:
    A -> 80+
    B -> 60-79
    C -> 50-59
    F -> below 50
    """
    graded_student = []
    for name, score in student_list:
        if score >= 80:
            grade = "A"
        elif score >= 60:
            grade = "B"
        elif score >= 50:
            grade = "C"
        else:
            grade = "F"
        graded_student.append((name, score, grade))
    return graded_student


print(calculate_average(students))
print(highest_student(students))
print(lowest_student(students))
print(passed_students(students))
print(failed_students(students))
print(list(add_bonus_marks(students)))
print(sort_students(students))
print(square_even_cube_odd(students))
print(students_above_70(students))
print(assign_grades(students))