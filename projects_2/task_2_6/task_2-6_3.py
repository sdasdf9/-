phenotype_d = input('Введите фенотип группы крови донора (I, II, III, IV): ').strip().upper()
phenotype_p = input('Введите фенотип группы крови пациента (I, II, III, IV): ').strip().upper()
if phenotype_d == phenotype_p or phenotype_d == 0:
    print('Возможно переливание крови')
else:
    print('Переливание невозможно')
