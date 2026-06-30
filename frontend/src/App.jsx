import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  async function sendMessage() {
    if (!message.trim()) return;

    const userMessage = message;

    setChat((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
    ]);

    setMessage("");

    try {
      const response = await fetch(
        "https://react-agent-langgraph.onrender.com/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: userMessage,
          }),
        }
      );

      console.log("Status:", response.status);

      const data = await response.json();

      console.log("API Response:", data);

      setChat((prev) => [
        ...prev,
        {
          role: "agent",
          content: data.response,
        },
      ]);
    } catch (error) {
      console.error("Fetch Error:", error);

      setChat((prev) => [
        ...prev,
        {
          role: "agent",
          content: "An error occurred while contacting the server.",
        },
      ]);
    }
  }

  return (
    <div>
      <h1>LangGraph AI Agent</h1>

      <div>
        {chat.map((item, index) => (
          <p key={index}>
            <b>{item.role}:</b> {item.content}
          </p>
        ))}
      </div>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;