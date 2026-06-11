students = [
 ("Abel", 45),
 ("Sara", 80),
 ("John", 66),
 ("Mahi", 30),
 ("Helen", 90)
]



"""
Exercise 1: Student Score Analyzer
Concepts Covered: Functions, Lists, Conditions, List Comprehension, Lambda, map()
Problem:
Create a program that stores student scores and calculates:
• average score
• highest score
• lowest score
• passed and failed students
• bonus marks using map()
• sorted students using lambda

"""
average = sum(score for name, score in students) / len(students)
print("Average Score:", average)
highest_score = max(score for name, score in students)
print("Highest Score:", highest_score)
lowest_score = min(score for name, score in students)
print("Lowest Score:", lowest_score)
pass_fail = [("Passed", name) if score >= 50 else ("Failed", name) for name, score in students]
print("Pass/Fail Status:", pass_fail)
bonus = map(lambda x: (x[0], x[1] + 30) if x[0] in ["Abel", "Mahi"] else x, students)
print("Bonus Marks:", list(bonus))
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted Students:", sorted_students)