n = int(input("Введите размер массива N: "))

arr = []
i = 0
while i < n:
    num = float(input(f"Введите элемент {i + 1}: "))
    arr.append(num)
    i = i + 1

sum_even_index = 0
count_even_index = 0
i = 0
while i < n:
    if i % 2 == 0:
        sum_even_index = sum_even_index + arr[i]
        count_even_index = count_even_index + 1
    i = i + 1

if count_even_index > 0:
    avg = sum_even_index / count_even_index
else:
    avg = 0

print("Среднее арифметическое элементов с чётными индексами:", avg)
