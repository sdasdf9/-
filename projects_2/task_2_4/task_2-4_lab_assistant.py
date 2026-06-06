volume = int(input('Введите нужный объем раствора: '))
salt_weight = volume * 0.009
water_volume = volume
with open('recipe.txt', 'w', encoding='utf-8') as report:
    report.write(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n')
    report.write(f'Общий объем: {volume} мл\n')
    report.write(f'Масса соли: {salt_weight:.2f} г\n')
    report.write(f'Объем воды: {water_volume} мл\n')
