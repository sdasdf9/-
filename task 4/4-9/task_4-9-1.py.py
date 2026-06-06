print("Программа находит максимальное из двух чисел")


x = float(input("Введите первое число X: "))
y = float(input("Введите второе число Y: "))


if x > y:
    max_num = x
else:
    max_num = y


print("Максимальное число:", max_num)