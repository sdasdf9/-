from typing import List, Dict, Tuple, Any

def process_samples(records: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
    """
    Обрабатывает результаты анализов: конвертирует текстовые значения в числа 
    и присваивает категорию качества.

    Args:
        records (List[Dict[str, Any]]): Список словарей, где каждый словарь — это результат 
                                        анализа с ключами 'id' и 'value'.

    Returns:
        Tuple[List[Dict[str, Any]], List[str]]: Кортеж из двух списков. 
            Первый список — успешно обработанные словари с новым полем 'quality'.
            Второй список — текстовые сообщения об ошибках.
    """
    processed_records = []
    errors = []

    for record in records:
        # Безопасно получаем ID, если его нет — пишем 'Unknown'
        sample_id = record.get("id", "Unknown") 
        
        try:
            # 1. Пытаемся конвертировать строку в число
            val = float(record["value"])
            
            # 2. Определяем качество
            if val < 5:
                quality = "low"
            elif 5 <= val <= 10:
                quality = "normal"
            else:
                quality = "high"
                
            # 3. Добавляем данные (перезаписываем value на float и добавляем quality)
            # Делаем копию, чтобы не менять исходный список (хорошая практика)
            updated_record = record.copy()
            updated_record["value"] = val
            updated_record["quality"] = quality
            
            processed_records.append(updated_record)
            
        except ValueError as e:
            # Если float() упал, ловим ошибку значения
            errors.append(f"Sample {sample_id}: Невозможно преобразовать в число ({e})")
        except KeyError:
            # Если в словаре вообще нет ключа "value"
            errors.append(f"Sample {sample_id}: Отсутствует поле 'value'")

    return processed_records, errors

# ==========================================
# ТЕСТИРОВАНИЕ ФУНКЦИИ
# ==========================================

# Исходные данные: смесь хороших данных и с ошибками (опечатки, текст вместо числа)
raw_data = [
    {"id": "S-001", "value": "4.2"},      # Нормальная запись (low)
    {"id": "S-002", "value": "7.5"},      # Нормальная запись (normal)
    {"id": "S-003", "value": "12.1"},     # Нормальная запись (high)
    {"id": "S-004", "value": "error"},    # Ошибка: текст вместо числа
    {"id": "S-005"},                      # Ошибка: вообще нет поля value
    {"id": "S-006", "value": "8,3"}       # Ошибка: запятая вместо точки
]

# Вызываем функцию
good_samples, bad_samples = process_samples(raw_data)

# Выводим результаты
print("УСПЕШНО ОБРАБОТАННЫЕ ЗАПИСИ:")
for sample in good_samples:
    print(sample)

print("\nОШИБКИ:")
for err in bad_samples:
    print(err)