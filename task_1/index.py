from pathlib import Path

SALARY_FILE = Path('salary1.txt')


def total_salary(path):
    sum_salary = 0
    quantity_of_employee = 0
    if path.exists():
        with open(path) as file:
            for line in file:
                employee_name, salary = line.split(',', maxsplit=1)
                salary = salary.rstrip('\n')
                sum_salary += int(salary)
                quantity_of_employee += 1
    else:
        print(f'File {path} not exist!')
    average_salary = sum_salary / quantity_of_employee
    result = (sum_salary, int(average_salary))
    print(f'Summary salary = {result[0]}, average salary = {result[1]}')


total_salary(SALARY_FILE)
