students_dict = {
    "Іванов": ("Іван", 20, 85),
    "Петренко": ("Петро", 21, 90),
    "Кравченко": ("Олена", 19, 95),
    "Шевченко": ("Марія", 20, 88)
}

surname = input("Введіть прізвище студента: ")

if surname in students_dict:
    # Виводимо інформацію про студента
    name, age, score = students_dict[surname]
    print("Інформація про студента:")
    print("Прізвище:", surname)
    print("Ім'я:", name)
    print("Вік:", age)
    print("Оцінка:", score)
else:
    print("Студента з таким прізвищем не знайдено.")