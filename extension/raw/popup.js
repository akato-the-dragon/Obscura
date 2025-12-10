document.addEventListener('DOMContentLoaded', function() {
    const savePasswordsCheckbox = document.getElementById('savePasswords');
    const autoFillCheckbox = document.getElementById('autoFillPasswords');

    chrome.storage.local.get(['savePasswords', 'autoFillPasswords'], function(result) {
        savePasswordsCheckbox.checked = result.savePasswords !== false;
        autoFillCheckbox.checked = result.autoFillPasswords !== false;
    });
    
    savePasswordsCheckbox.addEventListener('change', function() {
        chrome.storage.local.set({ savePasswords: this.checked });
        sendSettingsToContentScript();
    });
    
    autoFillCheckbox.addEventListener('change', function() {
        chrome.storage.local.set({ autoFillPasswords: this.checked });
        sendSettingsToContentScript();
    });
    
    function sendSettingsToContentScript() {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            if (tabs[0]) {
                chrome.tabs.sendMessage(tabs[0].id, {
                    action: 'updateSettings',
                    savePasswords: savePasswordsCheckbox.checked,
                    autoFillPasswords: autoFillCheckbox.checked
                });
            }
        });
    }
    
    checkServiceConnection();
    
    const githubIcon = document.querySelector('.github-icon');
    if (githubIcon) {
        githubIcon.addEventListener('click', function(e) {
            e.preventDefault();
            chrome.tabs.create({ url: this.href });
        });
    }
});

async function checkServiceConnection() {
    try {
        const response = await fetch('http://localhost:8000/extension/ping', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            console.log('Service is connected');
        } else {
            console.log('Service is not responding');
        }
    } catch (error) {
        console.log('Service is offline');
    }
}