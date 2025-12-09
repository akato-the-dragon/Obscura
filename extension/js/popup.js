document.addEventListener('DOMContentLoaded', function() {
    // Загрузка настроек
    chrome.storage.sync.get(['savePasswords', 'autoFillPasswords'], function(data) {
        document.getElementById('savePasswords').checked = data.savePasswords !== false;
        document.getElementById('autoFillPasswords').checked = data.autoFillPasswords !== false;
    });

    // Сохранение настроек при изменении
    document.getElementById('savePasswords').addEventListener('change', function(e) {
        chrome.storage.sync.set({ savePasswords: e.target.checked });
    });

    document.getElementById('autoFillPasswords').addEventListener('change', function(e) {
        chrome.storage.sync.set({ autoFillPasswords: e.target.checked });
    });

    // Проверка состояния бэкенда (FastAPI)
    checkBackendStatus();
});

function checkBackendStatus() {
    const statusDiv = document.getElementById('backendStatus');
    const indicator = statusDiv.querySelector('.status-indicator');
    const textSpan = statusDiv.querySelector('span');

    fetch('http://localhost:8000/health')
        .then(response => {
            if (response.ok) {
                statusDiv.className = 'status ok';
                textSpan.textContent = 'Сервер доступен';
            } else {
                statusDiv.className = 'status error';
                textSpan.textContent = 'Сервер недоступен';
            }
        })
        .catch(() => {
            statusDiv.className = 'status error';
            textSpan.textContent = 'Сервер недоступен';
        });
}