// background.js

const BACKEND_URL = "http://127.0.0.1:8000";

// Отправка heartbeat каждые 10 секунд
async function sendHeartbeat() {
    try {
        await fetch(`${BACKEND_URL}/extension/heartbeat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: "obscura-extension" }),
            signal: AbortSignal.timeout ? AbortSignal.timeout(3000) : null
        });
    } catch (e) {
        // Игнорируем ошибки — расширение просто "молчит", если бэкенд выключен
    }
}

sendHeartbeat();
setInterval(sendHeartbeat, 10000);

// Обработка сообщений от content.js
chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
    const url = new URL(sender.url).hostname;

    if (request.action === "getCredentials") {
        try {
            const response = await fetch(`${BACKEND_URL}/credentials/${url}`, {
                method: "GET",
                signal: AbortSignal.timeout ? AbortSignal.timeout(3000) : null
            });

            if (response.ok) {
                const data = await response.json();
                sendResponse(data);
            } else {
                sendResponse(null);
            }
        } catch (e) {
            console.warn("Obscura: не удалось получить данные", e);
            sendResponse(null);
        }
    }

    else if (request.action === "saveCredentials") {
        try {
            const response = await fetch(`${BACKEND_URL}/credentials`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    site_url: url,
                    login: request.username,
                    password: request.password
                }),
                signal: AbortSignal.timeout ? AbortSignal.timeout(3000) : null
            });

            if (response.ok) {
                sendResponse({ success: true });
            } else {
                sendResponse({ success: false });
            }
        } catch (e) {
            console.warn("Obscura: не удалось сохранить пароль", e);
            sendResponse({ success: false });
        }
    }

    return true; // для асинхронных ответов
});