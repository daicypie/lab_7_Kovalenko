numbers = (10, 20, 30, 40, 50, 60)

n = int(input("Введіть число  n: "))

result = []
for num in numbers:
    if num < n:
        result.append(num)

print("Числа, менші за", n, ":", result)