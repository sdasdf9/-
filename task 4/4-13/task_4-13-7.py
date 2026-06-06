n = int(input("Введите размер массива N: "))

arr = []
i = 0
while i < n:
    num = float(input(f"Введите элемент {i + 1}: "))
    arr.append(num)
    i = i + 1

sum_arr = 0
i = 0
while i < n:
    sum_arr = sum_arr + arr[i]
    i = i + 1

avg = sum_arr / n

print("Среднее арифметическое всех элементов:", avg)