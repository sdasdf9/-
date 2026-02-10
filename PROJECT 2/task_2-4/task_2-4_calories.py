protein = float(input("Введите массу белков в продукте (г): "))
fat = float(input("Введите массу жиров в продукте (г): "))
carbs = float(input("Введите массу углеводов в продукте (г): "))

calories = (protein * 4) + (fat * 9) + (carbs * 4)

print(f"Общая калорийность продукта: {calories:.1f} ккал")