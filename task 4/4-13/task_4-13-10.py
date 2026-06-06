n = int(input("Введите размер массива N: "))

arr = []
i = 0
while i < n:
    num = float(input(f"Введите элемент {i + 1}: "))
    arr.append(num)
    i = i + 1

sum_odd_index = 0
i = 0
while i < n:
    if i % 2 != 0:
        sum_odd_index = sum_odd_index + arr[i]
    i = i + 1

print("Сумма элементов с нечётными индексами:", sum_odd_index)