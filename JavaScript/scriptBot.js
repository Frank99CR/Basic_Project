document.getElementById('input').addEventListener('keypress', async function (e) {
    if (e.key === 'Enter') {
        const input = e.target.value;
        if (!input.trim()) return;

        // Display user message
        addMessage(input, 'user');

        // Clear input
        e.target.value = '';

        try {
            // Call the API
            const response = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer`  //
                },
                body: JSON.stringify({
                    model: 'gpt-3.5-turbo',
                    messages: [{ role: 'user', content: input }]
                })
            });

            if (!response.ok) {
                if (response.status === 429) {
                    throw new Error('Rate limit exceeded. Please wait and try again.');
                } else {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
            }

            const data = await response.json();
            console.log(data);  // Log the complete response for debugging

            if (data.choices && data.choices.length > 0) {
                const botMessage = data.choices[0].message.content;
                // Display bot message
                addMessage(botMessage, 'bot');
            } else {
                throw new Error('No response from the API.');
            }

        } catch (error) {
            console.error('Error:', error);
            addMessage(`An error occurred: ${error.message}`, 'bot');
        }
    }
});

function addMessage(content, className) {
    const chat = document.getElementById('chat');
    const message = document.createElement('div');
    message.className = `message ${className}`;
    message.textContent = content;
    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;
}
