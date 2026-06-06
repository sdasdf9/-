products = [
    {"sku": "A1", "category": "flour", "expected": 100, "actual": 95},
    {"sku": "B2", "category": "sugar", "expected": 50, "actual": 50},
    {"sku": "C3", "category": "enzyme", "expected": 10, "actual": 12},
]

discrepancies = []
by_category = {}

for product in products:
    sku = product["sku"]
    category = product["category"]
    
    # 1. Находим расхождения
    diff = product["actual"] - product["expected"]
    if diff != 0:
        discrepancies.append((sku, diff))
        
    # 2. Группируем по категориям
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(sku)

print("Расхождения (discrepancies):", discrepancies)
print("Категории (by_category):", by_category)