all_caps = int(input('Введите общее количество произведенных капсул: '))
caps_in_pack = int(input('Введите количество капсул в одной упаковке: '))
full_packages = all_caps // caps_in_pack
remains = all_caps % caps_in_pack
print('---Отчет фасовочного цеха---')
print(f'Полных упаковок: {full_packages}')
print(f'Остаток капсул:\t{remains}')
