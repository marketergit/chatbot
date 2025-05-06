async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    addMessage("user", userMessage);
    userInput.value = "";

    const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    addMessage("ai", data.response);
}
