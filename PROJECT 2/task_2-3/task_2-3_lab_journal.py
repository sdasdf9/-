# Запрос данных у пользователя
researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату (например, 08.02.2026): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод эксперимента: ")

# Формирование рамки и содержимого
frame_width = 50
top_bottom = "+" + "-" * (frame_width - 2) + "+"

content = (
    f"{top_bottom}\n"
    f"| Электронный лабораторный журнал{' ' * (frame_width - 33)}|\n"
    f"{top_bottom}\n"
    f"| ФИО исследователя : {researcher_name}{' ' * (frame_width - len('| ФИО исследователя : ') - len(researcher_name) - 1)}|\n"
    f"| Дата{' ' * 12}: {date}{' ' * (frame_width - len('| Дата             : ') - len(date) - 1)}|\n"
    f"| Эксперимент{' ' * 7}: {experiment_name}{' ' * (frame_width - len('| Эксперимент      : ') - len(experiment_name) - 1)}|\n"
    f"{top_bottom}\n"
    f"| Вывод:{' ' * (frame_width - 9)}|\n"
)

# Разбивка вывода на строки с переносами
conclusion_lines = []
while conclusion:
    if len(conclusion) > frame_width - 4:
        # Находим место для разрыва строки
        split_index = conclusion.rfind(' ', 0, frame_width - 4)
        if split_index == -1:
            split_index = frame_width - 4
        conclusion_lines.append(conclusion[:split_index])
        conclusion = conclusion[split_index:].strip()
    else:
        conclusion_lines.append(conclusion)
        conclusion = ""

# Добавление строк вывода в содержание
for line in conclusion_lines:
    content += f"| {line}{' ' * (frame_width - len(line) - 3)}|\n"

content += f"{top_bottom}"

# Запись в файл
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Журнал успешно сохранён в файле 'journal.txt'.")