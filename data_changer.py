# Исходные переменные
created_date = "22-12-2024"
issue_date = "23-12-2024"

# Извлекаем день и месяц из created_date
temp_created_date = "-".join(created_date.split("-")[:2])

# Извлекаем день и месяц из issue_date
temp_issue_date = "-".join(issue_date.split("-")[:2])

# Выводим результаты
print("Дата создания:", temp_created_date)
print("Дата истечения:", temp_issue_date)