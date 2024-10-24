school_class = {}

while True:
    name = input("Введіть ім'я та прізвище студента: ")
    if name == '':
        break

    score = int(input("Введіть оцінку студента (0-10): "))
    if score not in range(0, 11):
        print("Оцінка повинна бути в межах від 0 до 10.")
        continue

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

print("\nСередній бал по предметах:")
for name in sorted(school_class.keys()):
    total = sum(school_class[name])
    count = len(school_class[name])
    average = total / count
    print(f"{name}: {average:.2f}")