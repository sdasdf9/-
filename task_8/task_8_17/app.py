import io
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, jsonify, send_file
from sqlalchemy import create_engine

app = Flask(__name__)

# Замените ВАШ_ПАРОЛЬ на ваш пароль от PostgreSQL
DB_URI = 'postgresql+psycopg2://postgres:student@localhost:5435/student_task'
ENGINE = create_engine(DB_URI)

@app.route('/')
def index():
    return render_template('index.html')

# --- СТАТИСТИКА ---
@app.route('/api/metric/mean')
def get_mean():
    df = pd.read_sql("SELECT price FROM prices", ENGINE)
    return jsonify({"label": "Средняя цена", "value": f"{df['price'].mean():.2f}"})

@app.route('/api/metric/median')
def get_median():
    df = pd.read_sql("SELECT price FROM prices", ENGINE)
    return jsonify({"label": "Медиана цен", "value": f"{df['price'].median():.2f}"})

@app.route('/api/metric/total')
def get_total():
    df = pd.read_sql("SELECT id FROM prices", ENGINE)
    return jsonify({"label": "Кол-во товаров", "value": len(df)})

@app.route('/api/metric/max')
def get_max():
    df = pd.read_sql("SELECT price FROM prices", ENGINE)
    return jsonify({"label": "Макс. цена", "value": f"{df['price'].max():.2f}"})

# --- ГРАФИКИ ---
@app.route('/api/chart/histogram')
def chart_histogram():
    df = pd.read_sql("SELECT price FROM prices", ENGINE)
    
    # Используем современный стиль
    plt.style.use('seaborn-v0_8-muted')
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Рисуем гистограмму с более красивыми цветами и обводкой
    n, bins, patches = ax.hist(df['price'].astype(float), bins=20, 
                               color='#5e81ac', alpha=0.8, edgecolor='white', linewidth=0.5)
    
    # Добавляем линию среднего значения
    mean_val = df['price'].mean()
    ax.axvline(mean_val, color='#bf616a', linestyle='--', linewidth=2, label=f'Среднее: {mean_val:.0f}')
    
    # Настройка осей и заголовка
    ax.set_title('Распределение товарных цен', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Цена', fontsize=12)
    ax.set_ylabel('Количество товаров', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    ax.legend()
    
    # Убираем лишние рамки (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=100) # dpi делает картинку четче
    buf.seek(0)
    plt.close()
    return send_file(buf, mimetype='image/png')

@app.route('/api/chart/bar')
def chart_bar():
    query = "SELECT p.name, pr.price FROM prices pr JOIN products p ON pr.product_id = p.id LIMIT 10"
    df = pd.read_sql(query, ENGINE)
    
    # Современный стиль
    plt.style.use('seaborn-v0_8-muted')
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Используем приятный глубокий голубой цвет
    ax.bar(df['name'], df['price'].astype(float), color='#88c0d0', edgecolor='#4c566a')
    
    # Настройка заголовка и осей
    ax.set_title('Топ-10 товаров по цене', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Цена', fontsize=12)
    
    # Поворот текста меток, чтобы они не накладывались
    plt.xticks(rotation=45, ha='right', fontsize=10)
    
    # Убираем лишние линии рамок
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    plt.close()
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)