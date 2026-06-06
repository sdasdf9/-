n = int(input("Введите N: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print(f"{n}! = {fact}")