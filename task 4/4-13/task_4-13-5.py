n = int(input("Введите количество чисел N: "))

max_num = float(input("Введите число 1: "))

i = 2
while i <= n:
    num = float(input(f"Введите число {i}: "))
    if num > max_num:
        max_num = num
    i = i + 1

print("Максимальное число:", max_num)