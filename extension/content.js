// ===== Obscura Password Manager =====
// Версия с сохранением и автозаполнением (без визуальных уведомлений)

console.log("Obscura: Password manager loaded");

// Глобальные настройки
let settings = {
  savePasswords: true,
  autoFillPasswords: true
};

// ===== ФУНКЦИЯ АВТОЗАПОЛНЕНИЯ =====
async function autoFillCredentials() {
  console.log("AutoFill: Checking for saved credentials...");
  
  if (!settings.autoFillPasswords) {
    console.log("AutoFill disabled in settings");
    return false;
  }
  
  // Поиск всех возможных полей логина
  const loginSelectors = [
    'input[type="email"]',
    'input[type="text"]',
    'input[name*="user"]',
    'input[name*="login"]',
    'input[name*="email"]',
    'input[id*="user"]',
    'input[id*="login"]',
    'input[id*="email"]',
    'input[autocomplete="username"]',
    'input[autocomplete="email"]'
  ];
  
  let loginField = null;
  for (const selector of loginSelectors) {
    loginField = document.querySelector(selector);
    if (loginField && loginField.offsetParent !== null) {
      break;
    }
  }
  
  // Поиск поля пароля
  const passwordField = document.querySelector('input[type="password"]');
  
  if (!loginField || !passwordField) {
    console.log("AutoFill: Login or password field not found");
    return false;
  }
  
  // Если поля уже заполнены, не перезаписываем
  if (loginField.value && passwordField.value) {
    console.log("AutoFill: Fields already filled");
    return false;
  }
  
  // Получаем домен
  const domain = window.location.hostname;
  console.log("AutoFill: Requesting credentials for domain:", domain);
  
  try {
    // Запрашиваем сохраненные данные из бэкенда
    const response = await chrome.runtime.sendMessage({
      action: "getCredentials",
      domain: domain
    });
    
    if (response && response.login && response.password) {
      console.log("AutoFill: Found saved credentials");
      
      // Заполняем поля
      let filled = false;
      
      if (!loginField.value) {
        loginField.value = response.login;
        triggerEvent(loginField, 'input');
        triggerEvent(loginField, 'change');
        console.log("AutoFill: Login field filled");
        filled = true;
      }
      
      if (!passwordField.value) {
        passwordField.value = response.password;
        triggerEvent(passwordField, 'input');
        triggerEvent(passwordField, 'change');
        console.log("AutoFill: Password field filled");
        filled = true;
      }
      
      return filled;
    } else {
      console.log("AutoFill: No saved credentials found");
      return false;
    }
  } catch (error) {
    console.error("AutoFill Error:", error);
    return false;
  }
}

// ===== ФУНКЦИЯ СОХРАНЕНИЯ =====
async function saveCredentials() {
  console.log("Save: Attempting to save credentials...");
  
  if (!settings.savePasswords) {
    console.log("Save: Password saving disabled");
    return false;
  }
  
  // Поиск полей
  const loginField = document.querySelector('input[type="email"], input[type="text"]');
  const passwordField = document.querySelector('input[type="password"]');
  
  if (!loginField || !passwordField) {
    console.warn("Save: Login or password field not found");
    return false;
  }
  
  const login = loginField.value?.trim();
  const password = passwordField.value?.trim();
  
  if (!login || !password) {
    console.warn("Save: Empty fields");
    return false;
  }
  
  const domain = window.location.href;
  
  try {
    const response = await chrome.runtime.sendMessage({
      action: "saveCredentials",
      domain,
      login,
      password
    });
    
    if (response && response.success) {
      console.log("Save: Credentials saved successfully");
      return true;
    } else {
      console.error("Save: Failed to save");
      return false;
    }
  } catch (error) {
    console.error("Save Error:", error);
    return false;
  }
}

// ===== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =====
function triggerEvent(element, eventName) {
  const event = new Event(eventName, { bubbles: true });
  element.dispatchEvent(event);
}

// ===== ИНИЦИАЛИЗАЦИЯ =====
async function initialize() {
  console.log("Obscura: Initializing...");
  
  // Загружаем настройки
  try {
    const storedSettings = await chrome.storage.local.get(['savePasswords', 'autoFillPasswords']);
    settings.savePasswords = storedSettings.savePasswords !== false;
    settings.autoFillPasswords = storedSettings.autoFillPasswords !== false;
    console.log("Settings loaded:", settings);
  } catch (error) {
    console.error("Failed to load settings:", error);
  }
  
  // Пытаемся автозаполнить при загрузке страницы
  if (settings.autoFillPasswords) {
    setTimeout(() => {
      autoFillCredentials();
    }, 1000);
  }
  
  // Слушаем изменения настроек в реальном времени
  chrome.storage.onChanged.addListener((changes, namespace) => {
    if (namespace === 'local') {
      if (changes.savePasswords) {
        settings.savePasswords = changes.savePasswords.newValue;
        console.log("Save passwords setting changed:", settings.savePasswords);
      }
      if (changes.autoFillPasswords) {
        settings.autoFillPasswords = changes.autoFillPasswords.newValue;
        console.log("AutoFill setting changed:", settings.autoFillPasswords);
      }
    }
  });
  
  // Обработчик отправки формы
  document.addEventListener('submit', async (e) => {
    console.log("Form submit detected");
    if (settings.savePasswords) {
      setTimeout(() => {
        saveCredentials();
      }, 100);
    }
  }, true);
  
  // Обработчик кликов по кнопкам входа
  document.addEventListener('click', async (e) => {
    const target = e.target;
    const isLoginButton = 
      target.type === 'submit' ||
      target.closest('[type="submit"]') ||
      (target.tagName === 'BUTTON' && /войти|login|sign|вход/i.test(target.textContent?.toLowerCase() || ''));
    
    if (isLoginButton && settings.savePasswords) {
      console.log("Login button clicked");
      setTimeout(() => {
        saveCredentials();
      }, 200);
    }
  }, true);
  
  // Мониторинг динамических форм
  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
        // Проверяем, добавились ли поля формы
        const hasNewForm = Array.from(mutation.addedNodes).some(node => {
          if (node.nodeType === 1) {
            return node.querySelector('input[type="email"], input[type="text"], input[type="password"]');
          }
          return false;
        });
        
        if (hasNewForm && settings.autoFillPasswords) {
          console.log("Dynamic form detected, attempting autofill...");
          setTimeout(() => {
            autoFillCredentials();
          }, 500);
        }
      }
    }
  });
  
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
  
  // Также пробуем автозаполнить при фокусе на поле
  document.addEventListener('focusin', (e) => {
    if (e.target.matches('input[type="email"], input[type="text"], input[type="password"]')) {
      if (settings.autoFillPasswords) {
        setTimeout(() => {
          autoFillCredentials();
        }, 300);
      }
    }
  }, true);
  
  console.log("Obscura: Initialization complete");
}

// Запускаем инициализацию
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initialize);
} else {
  initialize();
}
