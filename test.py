def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            # Розділяємо рядок на ім'я та зарплату, використовуючи кому як розділювач
            parts = line.strip().split(',')
            if len(parts) == 2:
                name, salary = parts
                try:
                    salary = float(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Invalid salary value for {name}: {salary}")
            else:
                print(f"Invalid line format: {line}")

        if count == 0:
            average = 0
        else:
            average = total / count

        return (total, average)

    except FileNotFoundError:
        print(f"The file {path} does not exist.")
        return


# Виклик функції та вивід результату
path = 'salary.txt'
result = total_salary(path)
if result:
    print(result)  # (загальна сума зарплат, середня зарплата)
