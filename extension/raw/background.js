const SERVICE_URL = 'http://localhost:8000';

let isServiceConnected = false;

async function checkServiceConnection() {
    try {
        const response = await fetch(`${SERVICE_URL}/extension/ping`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        isServiceConnected = response.ok;
        updateExtensionIcon();
        return isServiceConnected;
    } catch (error) {
        isServiceConnected = false;
        updateExtensionIcon();
        return false;
    }
}

function updateExtensionIcon() {
    const iconPath = isServiceConnected ? {
        "16": "icons/icon16.png",
        "48": "icons/icon48.png",
        "128": "icons/icon128.png"
    } : {
        "16": "icons/icon16-offline.png",
        "48": "icons/icon48-offline.png",
        "128": "icons/icon128-offline.png"
    };
    
    chrome.action.setIcon({ path: iconPath });
}

setInterval(checkServiceConnection, 15000);

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    switch (message.action) {
        case 'getCredentials':
            handleGetCredentials(message.domain, sendResponse);
            return true;
            
        case 'saveCredentials':
            handleSaveCredentials(message.data, sendResponse);
            return true;
            
        case 'checkService':
            sendResponse({ connected: isServiceConnected });
            break;
    }
});

async function handleGetCredentials(domain, sendResponse) {
    try {
        const response = await fetch(`${SERVICE_URL}/credentials/${encodeURIComponent(domain)}`);
        
        if (response.ok) {
            const credentials = await response.json();
            sendResponse({ success: true, credentials });
        } else {
            sendResponse({ success: false, error: 'Credentials not found' });
        }
    } catch (error) {
        sendResponse({ success: false, error: 'Service unavailable' });
    }
}

async function handleSaveCredentials(data, sendResponse) {
    try {
        const response = await fetch(`${SERVICE_URL}/credentials`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            sendResponse({ success: true });
        } else {
            sendResponse({ success: false, error: 'Failed to save' });
        }
    } catch (error) {
        sendResponse({ success: false, error: 'Service unavailable' });
    }
}

chrome.runtime.onStartup.addListener(() => {
    checkServiceConnection();
});

chrome.runtime.onInstalled.addListener(() => {
    checkServiceConnection();
    
    chrome.storage.local.set({
        savePasswords: true,
        autoFillPasswords: true
    });
});