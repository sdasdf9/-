a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))
d = float(input("Введите число D: "))

min_num = a

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d

print("Минимальное число:", min_num)