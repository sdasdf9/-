import json

def analyze_process_logs(jsonl_path, report_path):
    counts = {}
    total = 0
    
    with open(jsonl_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            log_entry = json.loads(line)
            level = log_entry["level"]
            
            if level not in counts:
                counts[level] = 0
            counts[level] += 1
            total += 1
            
    with open(report_path, 'w', encoding='utf-8') as report:
        report.write("Process Log Report\n")
        report.write("==================\n")
        
        for level, count in counts.items():
            report.write(f"{level}: {count}\n")
            
        report.write(f"Total: {total}\n")
        
    return counts

# ==========================================
# ТЕСТИРОВАНИЕ ФУНКЦИИ
# ==========================================

# 1. Создаем тестовый файл .jsonl, чтобы было что читать
sample_data = """{"timestamp": "2023-10-01T10:00:00", "level": "INFO", "message": "Нагрев начат"}
{"timestamp": "2023-10-01T10:05:00", "level": "INFO", "message": "Температура в норме"}
{"timestamp": "2023-10-01T10:06:00", "level": "WARNING", "message": "Давление скачет"}
{"timestamp": "2023-10-01T10:10:00", "level": "ERROR", "message": "Сбой датчика"}
{"timestamp": "2023-10-01T10:11:00", "level": "INFO", "message": "Перезапуск"}
"""

with open("test_logs.jsonl", "w", encoding="utf-8") as f:
    f.write(sample_data)

# 2. Запускаем нашу функцию
result_dict = analyze_process_logs("test_logs.jsonl", "summary_report.txt")

# 3. Выводим результаты на экран
print("Словарь, который вернула функция:")
print(result_dict)
print("\nСодержимое созданного файла отчета (summary_report.txt):")
with open("summary_report.txt", "r", encoding="utf-8") as f:
    print(f.read())