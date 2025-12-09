// Вспомогательная функция: найти форму логина
function findLoginForm() {
    const forms = document.querySelectorAll('form');
    for (let form of forms) {
        let usernameField = null;
        let passwordField = null;
        const inputs = form.querySelectorAll('input');
        for (let input of inputs) {
            if (input.type === 'text' || input.type === 'email' || input.type === 'username') {
                usernameField = input;
            } else if (input.type === 'password') {
                passwordField = input;
            }
        }
        if (usernameField && passwordField) {
            return { form, usernameField, passwordField };
        }
    }
    return null;
}

// === Автозаполнение при загрузке страницы ===
window.addEventListener('load', async () => {
    const loginForm = findLoginForm();
    if (!loginForm) return;

    const { autoFillPasswords } = await chrome.storage.sync.get('autoFillPasswords');
    if (autoFillPasswords === false) return;

    try {
        const response = await chrome.runtime.sendMessage({ action: "getCredentials" });
        if (response) {
            loginForm.usernameField.value = response.username;
            loginForm.passwordField.value = response.password;
            loginForm.usernameField.dispatchEvent(new Event('input', { bubbles: true }));
            loginForm.passwordField.dispatchEvent(new Event('input', { bubbles: true }));
        }
    } catch (e) {
        console.warn("Obscura: не удалось получить учётные данные");
    }
});

// === Автосохранение после отправки формы ===
document.addEventListener('submit', async (e) => {
    const loginForm = findLoginForm();
    if (!loginForm) return;

    const { savePasswords } = await chrome.storage.sync.get('savePasswords');
    if (savePasswords === false) return;

    const username = loginForm.usernameField.value.trim();
    const password = loginForm.passwordField.value;
    if (!username || !password) return;

    try {
        await chrome.runtime.sendMessage({
            action: "saveCredentials",
            username,
            password
        });
        // ТИХОЕ сохранение — без уведомлений
    } catch (e) {
        console.warn("Obscura: не удалось сохранить пароль");
    }
});