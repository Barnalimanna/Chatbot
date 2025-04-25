
document.addEventListener("DOMContentLoaded", () => {
  const userInput = document.getElementById("user-input");
  const container = document.querySelector(".container");

  // Create a message area dynamically
  const chatArea = document.createElement("div");
  chatArea.className = "chat-area";
  container.appendChild(chatArea);

  function addMessage(message, sender = "user") {
    const msg = document.createElement("div");
    msg.classList.add("message", sender === "user" ? "user-message" : "bot-message");
    msg.textContent = message;
    chatArea.appendChild(msg);
    chatArea.scrollTop = chatArea.scrollHeight;
  }

  function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    addMessage(message, "user");
    userInput.value = "";

    setTimeout(() => {
      addMessage("This is a sample bot reply.", "bot");
    }, 700);
  }
 // Send message on Enter key
 userInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") sendMessage();
});
});





