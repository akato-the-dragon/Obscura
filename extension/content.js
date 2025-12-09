// Перехватываем отправку форм входа
document.addEventListener("submit", async (e) => {
    const form = e.target;
    const usernameInput = form.querySelector('input[type="text"], input[type="email"], input[name*="user"], input[name*="login"]');
    const passwordInput = form.querySelector('input[type="password"]');

    if (usernameInput && passwordInput) {
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        if (username && password) {
            e.preventDefault(); // Останавливаем отправку формы

            chrome.runtime.sendMessage({
                action: "askSavePassword",
                url: window.location.origin,
                username,
                password
            }, (response) => {
                if (response?.status === "popup_opened") {
                    setTimeout(() => {
                        form.submit(); // Отправляем форму после закрытия popup
                    }, 1000);
                }
            });
        }
    }
});