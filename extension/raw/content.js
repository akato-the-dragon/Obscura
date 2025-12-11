let settings = {
    savePasswords: true,
    autoFillPasswords: true
};

chrome.storage.local.get(['savePasswords', 'autoFillPasswords'], function(result) {
    settings.savePasswords = result.savePasswords !== false;
    settings.autoFillPasswords = result.autoFillPasswords !== false;
    
    if (settings.autoFillPasswords) {
        autoFillCredentials();
    }
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'updateSettings') {
        settings.savePasswords = message.savePasswords;
        settings.autoFillPasswords = message.autoFillPasswords;
        
        if (settings.autoFillPasswords) {
            autoFillCredentials();
        }
    }
});

async function autoFillCredentials() {
    if (!settings.autoFillPasswords) return;
    
    const site_url = window.location.origin;
    
    try {
        const response = await chrome.runtime.sendMessage({
            action: 'getCredentials',
            site_url: site_url
        });
        
        if (response.success && response.credentials) {
            fillForm(response.credentials);
        }
    } catch (error) {
        console.log('Auto-fill error:', error);
    }
}

function fillForm(credentials) {
    const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    
    let loginField = null;
    let passwordField = null;
    
    inputs.forEach(input => {
        const name = (input.name || '').toLowerCase();
        const id = (input.id || '').toLowerCase();
        const placeholder = (input.placeholder || '').toLowerCase();
        
        if (name.includes('login') || name.includes('email') || name.includes('username') ||
            id.includes('login') || id.includes('email') || id.includes('username') ||
            placeholder.includes('логин') || placeholder.includes('email') || placeholder.includes('username')) {
            loginField = input;
        }
        
        if (name.includes('password') || id.includes('password') || 
            placeholder.includes('пароль')) {
            passwordField = input;
        }
    });
    
    if (loginField && credentials.login) {
        loginField.value = credentials.login;
        loginField.dispatchEvent(new Event('input', { bubbles: true }));
        loginField.dispatchEvent(new Event('change', { bubbles: true }));
    }
    
    if (passwordField && credentials.password) {
        passwordField.value = credentials.password;
        passwordField.dispatchEvent(new Event('input', { bubbles: true }));
        passwordField.dispatchEvent(new Event('change', { bubbles: true }));
    }
}

document.addEventListener('submit', async function(event) {
    if (!settings.savePasswords) return;
    
    const form = event.target;
    const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    
    let login = '';
    let password = '';
    let hasPassword = false;
    
    inputs.forEach(input => {
        if (input.type === 'password' && input.value) {
            password = input.value;
            hasPassword = true;
        } else if ((input.type === 'text' || input.type === 'email') && input.value) {
            login = input.value;
        }
    });

    if (hasPassword && login && password) {
        const site_url = window.location.origin;
        
        try {
            await chrome.runtime.sendMessage({
                action: 'saveCredentials',
                data: {
                    site_url: site_url,
                    login: login,
                    password: password
                }
            });
            
            console.log('Credentials saved for:', site_url);
        } catch (error) {
            console.log('Failed to save credentials:', error);
        }
    }
});

document.addEventListener('click', function(event) {
    if (!settings.savePasswords) return;
    
    const button = event.target.closest('button, input[type="submit"]');
    if (button) {
        setTimeout(() => {
            const form = button.closest('form');
            if (form) {
                const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
                
                let login = '';
                let password = '';
                let hasPassword = false;
                
                inputs.forEach(input => {
                    if (input.type === 'password' && input.value) {
                        password = input.value;
                        hasPassword = true;
                    } else if ((input.type === 'text' || input.type === 'email') && input.value) {
                        login = input.value;
                    }
                });
                
                if (hasPassword && login && password) {
                    const site_url = window.location.origin;
                    
                    chrome.runtime.sendMessage({
                        action: 'saveCredentials',
                        data: {
                            site_url: site_url,
                            login: login,
                            password: password
                        }
                    }).catch(console.error);
                }
            }
        }, 100);
    }
});

document.addEventListener('focusin', function(event) {
    if (event.target.type === 'password' && settings.autoFillPasswords) {
        setTimeout(autoFillCredentials, 500);
    }
});