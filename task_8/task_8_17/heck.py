from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>УРА! СЕРВЕР ЖИВ!</h1>"

if __name__ == '__main__':
    print("Запускаю тест на порту 8080...", flush=True)
    app.run(host='0.0.0.0', port=8080)