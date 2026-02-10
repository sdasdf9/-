volume_ml = float(input("Введите нужный объем раствора (мл): "))
salt_mass = volume_ml * 0.009
water_volume = volume_ml
recipe_text = f"Рецепт физиологического раствора (0.9%):\n"
recipe_text += f"1. Объем раствора: {volume_ml} мл\n"
recipe_text += f"2. Масса NaCl: {salt_mass:.2f} г\n"
recipe_text += f"3. Объем воды: {water_volume} мл\n"
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(recipe_text)
print(f"Рецепт сохранен в файл 'recipe.txt'.")