document.addEventListener('DOMContentLoaded', () => {
    const resultArea = document.getElementById('result-area');
    const actionButtons = document.querySelectorAll('.action-btn:not(.clear)');
    const clearButton = document.getElementById('clear-btn');

    // Функция отрисовки состояний
    const renderState = (state, message = '') => {
        if (state === 'loading') {
            resultArea.innerHTML = `<div class="loading">⏳ Выполняется запрос к БД...</div>`;
        } else if (state === 'error') {
            resultArea.innerHTML = `<div class="error">❌ Ошибка: ${message}</div>`;
        } else if (state === 'clear') {
            resultArea.innerHTML = `<p class="placeholder">← Выберите метрику или график в панели слева</p>`;
        }
    };

    // Обработчик для кнопок логики
    actionButtons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const action = btn.dataset.action; // 'metric' или 'chart'
            const path = btn.dataset.path;     // 'mean', 'histogram' и т.д.
            const url = `/api/${action}/${path}`;

            renderState('loading');

            try {
                const response = await fetch(url);
                
                if (!response.ok) throw new Error(`Сервер ответил со статусом ${response.status}`);

                if (action === 'metric') {
                    // Обрабатываем как JSON
                    const data = await response.json();
                    resultArea.innerHTML = `
                        <div class="stat-card">
                            <div class="label">${data.label}</div>
                            <div class="value">${data.value}</div>
                        </div>
                    `;
                } else if (action === 'chart') {
                    // Обрабатываем как картинку (Blob)
                    const blob = await response.blob();
                    const imgUrl = URL.createObjectURL(blob);
                    resultArea.innerHTML = `
                        <div class="chart-container">
                            <img src="${imgUrl}" alt="График ${path}">
                        </div>
                    `;
                }
            } catch (error) {
                console.error("Fetch Error:", error);
                renderState('error', error.message);
            }
        });
    });

    // Обработчик очистки
    clearButton.addEventListener('click', () => renderState('clear'));
});