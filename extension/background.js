let savedPasswordData = null;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "askSavePassword") {
        savedPasswordData = message;
        chrome.tabs.create({
            url: chrome.runtime.getURL("popup.html?mode=save"),
            active: true
        });
        sendResponse({ status: "popup_opened" });
    } else if (message.action === "getSavedData") {
        sendResponse(savedPasswordData);
    }
});