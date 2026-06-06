n = int(input("Введите N: "))

sum_n = 0
i = 1

while i <= n:
    sum_n = sum_n + i
    i = i + 1

print(f"Сумма чисел от 1 до {n}: {sum_n}")