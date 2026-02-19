donor = input("Введите группу крови донора (0, A, B, AB): ")
recipient = input("Введите группу крови реципиента (0, A, B, AB): ")

if donor == "0":
    print("Переливание возможно")
elif donor == recipient:
    print("Переливание возможно")
else:
    print("Переливание невозможно")