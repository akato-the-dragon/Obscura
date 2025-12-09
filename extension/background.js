const API_BASE = "http://127.0.0.1:8000";

// Проверка связи с бэкендом
async function checkBackendConnection() {
  try {
    const response = await fetch(`${API_BASE}/extension/ping`, {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    return response.ok;
  } catch (err) {
    return false;
  }
}

// Отправляем пинг при запуске
chrome.runtime.onInstalled.addListener(() => {
  checkBackendConnection();
});

// Обработка запросов из content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getCredentials") {
    fetch(`${API_BASE}/credentials/${encodeURIComponent(request.domain)}`)
      .then(res => {
        if (res.ok) return res.json();
        if (res.status === 404) return null;
        throw new Error(`HTTP ${res.status}`);
      })
      .then(data => sendResponse(data))
      .catch(() => sendResponse(null));
    
    return true;
  }
  
  if (request.action === "saveCredentials") {
    fetch(`${API_BASE}/credentials`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        domain: request.domain,
        login: request.login,
        password: request.password
      })
    })
    .then(response => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then(data => sendResponse({ success: true, data }))
    .catch(error => sendResponse({ success: false, error: error.message }));
    
    return true;
  }
  
  if (request.action === "checkConnection") {
    checkBackendConnection().then(isConnected => {
      sendResponse({ connected: isConnected });
    });
    return true;
  }
  
  sendResponse({ success: false, error: "Unknown action" });
});

// Периодическая проверка бэкенда
setInterval(checkBackendConnection, 30000);