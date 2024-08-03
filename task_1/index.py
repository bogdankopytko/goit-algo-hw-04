SALARY_FILE = 'salary0.txt'


def total_salary(path):
    sum_salary = 0
    quantity_of_employee = 0
    try:
        with open(path) as file:
            for line in file:
                employee_name, salary = line.split(',', maxsplit=1)
                salary = salary.rstrip('\n')
                sum_salary += float(salary)
                quantity_of_employee += 1
    except FileNotFoundError:
        return print(f'File {path} does not exist!')
    average_salary = sum_salary / quantity_of_employee
    return sum_salary, average_salary


if total_salary(SALARY_FILE):
    total, average = total_salary(SALARY_FILE)
    print(f'Summary salary = {total}, average salary = {average}')
