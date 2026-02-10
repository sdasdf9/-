print("Hello World!")
name = "Маловецкий Марк"
group = "4731901/50002"
score = 95
while True:
        chislo = int(input("Введите число от 1 до 5: "))
        if 1 <= chislo <= 5:
            break
        else:
            print("Пожалуйста, введите число в диапазоне от 1 до 7.")
if chislo == 1:
 print("Фамилия: Маловецкий", "Имя: Марк", "Группа: 4731901/50002", "Год: 2025")
elif chislo == 2:
 print(5, 2, 2026, sep=':')
elif chislo == 3:
 print("Предмет\t\tОценка")
 print("Математика\t5")
 print("Физика\t\t4")
 print("Информатика\t5")
elif chislo == 4:
 print(f"Студент {name} из группы {group} получил {score} баллов.")
elif chislo == 5:
 f = open("/Users/michael/Downloads/output.txt", "w", encoding="utf-8")
 print("Фамилия: Маловецкий", "Имя: Марк", "Группа: 4731901/50002", "Год: 2025")
 f.close()
elif chislo == 6:
 print("=================")
 print("Добро пожаловать")
 print("Студент 1 курса")
 print("2025 г")
 print("Удачи в обучении!")
 print("=================")