n = int(input("Введите размер массива N: "))

arr = []
i = 0
while i < n:
    num = float(input(f"Введите элемент {i + 1}: "))
    arr.append(num)
    i = i + 1

count = 0
i = 0
while i < n:
    if arr[i] > 0:
        count = count + 1
    i = i + 1

print("Количество положительных чисел:", count)