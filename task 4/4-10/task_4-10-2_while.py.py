
print("Программа находит сумму всех чётных чисел от 1 до 15")
sum_even = 0
i = 1
while i <= 15:
    if i % 2 == 0: 
        sum_even = sum_even + i
        print(f"Добавляем {i}, текущая сумма: {sum_even}")
    i = i + 1
print(f"\nСумма всех чётных чисел от 1 до 15: {sum_even}")