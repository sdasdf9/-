def parse_config(text):
    config = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()
    return config
# Пример данных
data = """
TEMP=37.5
# Настройки оборотов
AGITATION_RPM=250
"""

# Вызов функции и сохранение результата в переменную
result = parse_config(data)

# Команда для вывода результата на экран
print(result)