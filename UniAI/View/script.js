// DOM elementleri
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendButton = document.querySelector('.btn-primary');

// API adresi
const API_CONFIG = {
    university: 'http://127.0.0.1:8080'  // Flask default port
};

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    }

    if (userInput) {
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        userInput.focus();
    }
});

// Mesaj gönderme işlemi
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Kullanıcı mesajını ekle
    addMessage(message, 'user');
    userInput.value = '';

    // Yazıyor göstergesi
    const typingIndicator = addTypingIndicator();

    try {
        // API'ye istek gönder
        const response = await fetch(`${API_CONFIG.university}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                message: message,
                chat_history: []  // ya da önceki mesajların bir dizisi
            })
        });

        const data = await response.json();

        // Yazıyor göstergesini kaldır
        removeTypingIndicator(typingIndicator);

        // Bot yanıtını ekle (API'den gelen cevaptan 'answer' alınıyor)
        addMessage(data.response.answer, 'bot');
    } catch (error) {
        console.error('Hata:', error);
        removeTypingIndicator(typingIndicator);
        addMessage('Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.', 'bot');
    }
}

// Mesaj ekleme fonksiyonu
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    // Markdown metnini HTML olarak parse et
    const htmlContent = marked.parse(message);

    // Güvenlik açısından dikkat: Eğer API'den gelen içerik kontrolsüzse sanitize gerekebilir
    messageDiv.innerHTML = htmlContent;

    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Yazıyor göstergesi fonksiyonları
function addTypingIndicator() {
    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'typing-indicator';
    typingIndicator.innerHTML = `<span></span><span></span><span></span>`;
    chatContainer.appendChild(typingIndicator);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return typingIndicator;
}

function removeTypingIndicator(typingIndicator) {
    if (typingIndicator && chatContainer.contains(typingIndicator)) {
        chatContainer.removeChild(typingIndicator);
    }
}