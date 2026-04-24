const chatForm = document.getElementById('chat-form');
const newsInput = document.getElementById('news-input');
const chatMessages = document.getElementById('chat-messages');

function appendMessage(text, sender, predictionData = null) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);

    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    avatar.textContent = sender === 'user' ? '👤' : '🛡️';

    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    
    if (predictionData && sender === 'bot') {
        const badge = document.createElement('div');
        const isFake = predictionData.prediction === 'Fake News';
        badge.classList.add('prediction-badge', isFake ? 'fake' : 'real');
        badge.textContent = `${predictionData.prediction} (${predictionData.confidence.toFixed(1)}% confident)`;
        bubble.appendChild(badge);
        
        const textNode = document.createElement('p');
        textNode.textContent = predictionData.message;
        bubble.appendChild(textNode);
    } else {
        bubble.textContent = text;
    }

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(bubble);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTypingIndicator() {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'bot');
    messageDiv.id = 'typing-indicator';

    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    avatar.textContent = '🛡️';

    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    bubble.innerHTML = `
        <div class="typing-indicator">
            <span></span><span></span><span></span>
        </div>
    `;

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(bubble);
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.remove();
    }
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = newsInput.value.trim();
    if (!text) return;

    // Append user message
    appendMessage(text, 'user');
    newsInput.value = '';

    // Show typing
    showTypingIndicator();

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        const data = await response.json();
        removeTypingIndicator();
        
        // Append bot response
        appendMessage(null, 'bot', data);

    } catch (error) {
        console.error("Error:", error);
        removeTypingIndicator();
        appendMessage("Sorry, I'm having trouble connecting to my server. Please try again later.", 'bot', null);
    }
});
