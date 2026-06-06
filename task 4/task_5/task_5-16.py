import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",               # ← было 5432, стало 5435
        user="postgres",
        password="student",        # ← было example, стало student
        database="student_task"    # ← было testdb, стало student_task
    )

    cursor = connection.cursor()

    cursor.execute("SELECT id, name, category FROM products LIMIT 5;")

    rows = cursor.fetchall()

    print("Товары из таблицы products:")
    for row in rows:
        print(f"ID: {row[0]}, Название: {row[1]}, Категория: {row[2]}")

    cursor.close()
    connection.close()

    print("\nЗапрос выполнен успешно!")

except Exception as error:
    print(f"Ошибка при подключении или выполнении запроса: {error}")