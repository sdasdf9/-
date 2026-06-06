n = int(input("Введите N: "))

sum_squares = 0
i = 1

while i <= n:
    sum_squares = sum_squares + i * i
    i = i + 1

print(f"Сумма квадратов от 1 до {n}: {sum_squares}")