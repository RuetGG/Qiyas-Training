
# =====================================================
# Exercise 2: Employee Salary Management System
# =====================================================

employees = [
    ("John", "Developer", 5000),
    ("Sara", "Manager", 8000),
    ("Mike", "Designer", 4500),
    ("Helen", "Developer", 6500),
    ("David", "Manager", 7200)
]


def highest_paid_employee(employee_list):
    """
    Return highest paid employee.
    """
    return max(salary for name, dept, salary in employee_list)


def average_salary(employee_list):
    """
    Calculate average salary.
    """
    return sum(salary for name, dept, salary in employee_list) // len(employee_list)


def employees_above_average(employee_list):
    """
    Return employees earning above average salary.
    """
    avg = sum(salary for name, dept, salary in employee_list) // len(employee_list)
    # return (e if e >= avg for name, dept, e in employee_list)


def add_salary_bonus(employee_list):
    """
    Add 10% bonus salary using map().
    """
    pass


def sort_by_salary(employee_list):
    """
    Sort employees by salary descending.
    """
    pass


def double_low_salaries(employee_list):
    """
    Create a list with doubled salaries
    for salaries below 6000.
    """
    pass


def developers_only(employee_list):
    """
    Use filter() to return only developers.
    """
    pass