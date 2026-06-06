name = input('Название питательной среды: ')
concentration = input('Концентрацию агара (%): ')
temp = input('Температуру стерилизации: ')
with open('recipe.txt', "w", encoding="utf-8") as file:
    file.write(f"{name}\n")
    file.write("Параметры:\n")
    file.write(f"- Концентрация агара: {concentration}%\n")
    file.write(f"- Температура стерилизации: {temp}°C\n")
print("Файл 'recipe.txt' успешно сформирован!")
