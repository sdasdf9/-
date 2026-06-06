name = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па): ')
with open('sensor_log.txt', "w", encoding="utf-8") as file:
    file.write(f"{name}\t{pressure}\n")
    print('Данные успешно сохранены в sensor_log.txt') 
