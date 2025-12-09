document.addEventListener('DOMContentLoaded', () => {
  const saveToggle = document.getElementById('savePasswords');
  const autoFillToggle = document.getElementById('autoFillPasswords');
  
  // Загружаем текущие настройки
  chrome.storage.local.get(['savePasswords', 'autoFillPasswords'], (data) => {
    saveToggle.checked = data.savePasswords !== false;
    autoFillToggle.checked = data.autoFillPasswords !== false;
  });
  
  // Сохраняем изменения
  saveToggle.addEventListener('change', () => {
    chrome.storage.local.set({ savePasswords: saveToggle.checked });
  });
  
  autoFillToggle.addEventListener('change', () => {
    chrome.storage.local.set({ autoFillPasswords: autoFillToggle.checked });
  });
});