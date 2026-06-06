import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Настройка стиля графиков
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (12, 8)

print("="*80)
print("АНАЛИЗ ДАННЫХ ТАБЛИЦ products И prices")
print("="*80)

try:
    # 1. Подключение к базе данных
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("\n✓ Подключение к базе данных установлено")
    
    # 2. Извлечение данных
    query = """
    SELECT 
        p.id AS product_id,
        p.name AS product_name,
        p.category,
        pr.price,
        pr.created_at
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    ORDER BY pr.created_at
    """
    
    df = pd.read_sql(query, connection)
    print(f"✓ Загружено записей: {len(df)}")
    print(f"✓ Уникальных товаров: {df['product_id'].nunique()}")
    print(f"✓ Уникальных категорий: {df['category'].nunique()}")
    
    connection.close()
    print("✓ Соединение закрыто\n")
    
    # Расчёт статистических метрик
    stats_metrics = {
        'Среднее': df['price'].mean(),
        'Медиана': df['price'].median(),
        'Стандартное отклонение': df['price'].std(),
        'Минимум': df['price'].min(),
        'Максимум': df['price'].max(),
        'Q1 (25-й перцентиль)': df['price'].quantile(0.25),
        'Q3 (75-й перцентиль)': df['price'].quantile(0.75)
    }
    
    print("="*80)
    print("СТАТИСТИЧЕСКИЕ МЕТРИКИ ЦЕН")
    print("="*80)
    for key, value in stats_metrics.items():
        print(f"{key:25}: {value:.2f} руб.")
    
    # Поиск аномалий методом IQR
    Q1 = stats_metrics['Q1 (25-й перцентиль)']
    Q3 = stats_metrics['Q3 (75-й перцентиль)']
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    anomalies = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    
    print(f"\nМежквартильный размах (IQR): {IQR:.2f} руб.")
    print(f"Нижняя граница нормы: {lower_bound:.2f} руб.")
    print(f"Верхняя граница нормы: {upper_bound:.2f} руб.")
    
    if len(anomalies) > 0:
        print(f"\n⚠️ ОБНАРУЖЕНО АНОМАЛИЙ: {len(anomalies)}")
    else:
        print("\n✓ Аномалии не обнаружены")
    
    # СОЗДАНИЕ ГРАФИКОВ
    fig = plt.figure(figsize=(16, 12))
    
    # ГРАФИК 1: Гистограмма распределения цен
    ax1 = fig.add_subplot(2, 2, 1)
    sns.histplot(df['price'], bins=30, kde=True, ax=ax1, color='steelblue', edgecolor='black')
    
    ax1.axvline(stats_metrics['Среднее'], color='red', linestyle='-', linewidth=2, 
                label=f"Среднее: {stats_metrics['Среднее']:.0f} руб.")
    ax1.axvline(stats_metrics['Медиана'], color='green', linestyle='--', linewidth=2, 
                label=f"Медиана: {stats_metrics['Медиана']:.0f} руб.")
    ax1.axvline(stats_metrics['Q1 (25-й перцентиль)'], color='orange', linestyle=':', linewidth=2, 
                label=f"Q1: {stats_metrics['Q1 (25-й перцентиль)']:.0f} руб.")
    ax1.axvline(stats_metrics['Q3 (75-й перцентиль)'], color='purple', linestyle=':', linewidth=2, 
                label=f"Q3: {stats_metrics['Q3 (75-й перцентиль)']:.0f} руб.")
    
    ax1.set_xlabel('Цена (руб.)', fontsize=11)
    ax1.set_ylabel('Частота', fontsize=11)
    ax1.set_title('Распределение цен товаров с отображением статистических метрик', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # ГРАФИК 2: Boxplot по категориям
    ax2 = fig.add_subplot(2, 2, 2)
    categories_order = df.groupby('category')['price'].median().sort_values(ascending=False).index
    sns.boxplot(data=df, x='category', y='price', order=categories_order, ax=ax2, palette='Set2')
    
    ax2.set_xlabel('Категория товара', fontsize=11)
    ax2.set_ylabel('Цена (руб.)', fontsize=11)
    ax2.set_title('Распределение цен по категориям (Boxplot)', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    # ГРАФИК 3: Динамика цен по времени
    ax3 = fig.add_subplot(2, 2, 3)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date
    daily_prices = df.groupby('date')['price'].agg(['mean', 'median']).reset_index()
    
    ax3.plot(daily_prices['date'], daily_prices['mean'], marker='o', linewidth=2, 
             label='Средняя цена', color='darkblue')
    ax3.plot(daily_prices['date'], daily_prices['median'], marker='s', linewidth=2, 
             label='Медианная цена', color='darkorange')
    
    ax3.set_xlabel('Дата', fontsize=11)
    ax3.set_ylabel('Цена (руб.)', fontsize=11)
    ax3.set_title('Динамика цен во времени', fontsize=12, fontweight='bold')
    ax3.legend(loc='best', fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    
    # ГРАФИК 4: Количество записей по категориям
    ax4 = fig.add_subplot(2, 2, 4)
    category_counts = df['category'].value_counts()
    colors = sns.color_palette('Set3', len(category_counts))
    wedges, texts, autotexts = ax4.pie(category_counts.values, labels=category_counts.index, 
                                        autopct='%1.1f%%', colors=colors, startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    ax4.set_title('Распределение записей о ценах по категориям', fontsize=12, fontweight='bold')
    
    plt.suptitle('ВИЗУАЛИЗАЦИЯ АНАЛИЗА ЦЕН ТОВАРОВ', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    plt.savefig('price_analysis_charts.png', dpi=150, bbox_inches='tight')
    print("\n✓ Графики сохранены в файл: price_analysis_charts.png")
    
    plt.show()
    
except Exception as error:
    print(f"\n❌ Ошибка: {error}")
    import traceback
    traceback.print_exc()