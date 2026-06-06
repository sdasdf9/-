vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

scalar_product = 0
i = 0

while i < len(vector1):
    scalar_product += vector1[i] * vector2[i]
    i += 1

print("Скалярное произведение векторов:", scalar_product)