vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

scalar_product = 0

for i in range(len(vector1)):
    scalar_product += vector1[i] * vector2[i]

print("Скалярное произведение векторов:", scalar_product)