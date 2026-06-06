n = int(input("Введите размер массива N: "))

arr = []
i = 0
while i < n:
    num = float(input(f"Введите элемент {i + 1}: "))
    arr.append(num)
    i = i + 1

sum_odd = 0
i = 0
while i < n:
    if arr[i] % 2 != 0:
        sum_odd = sum_odd + arr[i]
    i = i + 1

print("Сумма нечётных элементов:", sum_odd)