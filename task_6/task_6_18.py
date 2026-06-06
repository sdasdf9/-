import psycopg2
import statistics

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("Подключение к базе данных успешно установлено!")
    
    cursor = connection.cursor()
    
    # 2. Выполнение JOIN-запроса
    query = """
    SELECT 
        p.name AS product_name,
        p.category,
        pr.price
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Извлекаем данные в списки
    products = []
    categories = []
    prices = []
    
    for row in rows:
        products.append(row[0])
        categories.append(row[1])
        prices.append(row[2])
    
    print(f"\nЗагружено записей: {len(prices)}")
    
    # 3. Основные статистические показатели
    print("\n" + "="*60)
    print("ОСНОВНЫЕ СТАТИСТИЧЕСКИЕ ПОКАЗАТЕЛИ ЦЕН")
    print("="*60)
    print(f"Среднее значение:         {statistics.mean(prices):.2f} руб.")
    print(f"Медиана:                  {statistics.median(prices):.2f} руб.")
    print(f"Стандартное отклонение:   {statistics.stdev(prices):.2f} руб.")
    print(f"Минимальная цена:         {min(prices):.2f} руб.")
    print(f"Максимальная цена:        {max(prices):.2f} руб.")
    
    # 4. Квартили
    sorted_prices = sorted(prices)
    n = len(sorted_prices)
    
    Q1 = sorted_prices[n // 4]
    Q2 = statistics.median(sorted_prices)
    Q3 = sorted_prices[3 * n // 4]
    IQR = Q3 - Q1
    
    print("\n" + "="*60)
    print("КВАРТИЛИ И МЕЖКВАРТИЛЬНЫЙ РАЗМАХ")
    print("="*60)
    print(f"Первый квартиль (Q1):     {Q1:.2f} руб.")
    print(f"Второй квартиль (Q2):     {Q2:.2f} руб.")
    print(f"Третий квартиль (Q3):     {Q3:.2f} руб.")
    print(f"Межквартильный размах:    {IQR:.2f} руб.")
    
    # Товары с ценой выше Q3
    print(f"\nТовары с ценой выше Q3:")
    print("-" * 50)
    for i, price in enumerate(prices):
        if price > Q3:
            print(f"Товар: {products[i]:30} | Категория: {categories[i]:20} | Цена: {price:.2f} руб.")
    
    # 5. Статистика по категориям
    print("\n" + "="*60)
    print("СТАТИСТИКА ПО КАТЕГОРИЯМ")
    print("="*60)
    
    categories_unique = set(categories)
    cat_stats = []
    
    for cat in categories_unique:
        cat_prices = [prices[i] for i in range(len(prices)) if categories[i] == cat]
        cat_stats.append({
            'category': cat,
            'count': len(cat_prices),
            'mean': statistics.mean(cat_prices),
            'median': statistics.median(cat_prices),
            'std': statistics.stdev(cat_prices) if len(cat_prices) > 1 else 0
        })
    
    cat_stats.sort(key=lambda x: x['mean'], reverse=True)
    
    for stat in cat_stats:
        print(f"\nКатегория: {stat['category']}")
        print(f"  Количество записей:      {stat['count']}")
        print(f"  Средняя цена:            {stat['mean']:.2f} руб.")
        print(f"  Медиана:                 {stat['median']:.2f} руб.")
        print(f"  Стандартное отклонение:  {stat['std']:.2f} руб.")
    
    # 6. Товары с наибольшим разбросом цен
    print("\n" + "="*60)
    print("ТОП-5 ТОВАРОВ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН")
    print("="*60)
    
    # Группируем по товарам
    product_prices = {}
    for i, product in enumerate(products):
        if product not in product_prices:
            product_prices[product] = []
        product_prices[product].append(prices[i])
    
    # Рассчитываем разброс
    price_ranges = []
    for product, price_list in product_prices.items():
        min_price = min(price_list)
        max_price = max(price_list)
        price_range = max_price - min_price
        price_ranges.append((product, min_price, max_price, price_range))
    
    # Сортируем по разбросу
    price_ranges.sort(key=lambda x: x[3], reverse=True)
    
    for i in range(min(5, len(price_ranges))):
        product, min_p, max_p, range_p = price_ranges[i]
        print(f"\nТовар: {product}")
        print(f"  Минимальная цена:  {min_p:.2f} руб.")
        print(f"  Максимальная цена: {max_p:.2f} руб.")
        print(f"  Разброс:           {range_p:.2f} руб.")
    
    cursor.close()
    connection.close()
    print("\n" + "="*60)
    print("Соединение закрыто.")
    
except Exception as error:
    print(f"Ошибка: {error}")