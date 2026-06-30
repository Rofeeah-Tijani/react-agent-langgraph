import { useState } from "react"


function App() {

  const [message, setMessage] = useState("")
  const [chat, setChat] = useState([])


  async function sendMessage() {

    if (!message.trim()) return


    const userMessage = message


    setChat(prev => [
      ...prev,
      {
        role: "user",
        content: userMessage
      }
    ])


    setMessage("")


    const response = await fetch(
      "https://react-agent-langgraph.onrender.com/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: userMessage
        })
      }
    )


    const data = await response.json()


    setChat(prev => [
      ...prev,
      {
        role: "agent",
        content: data.response
      }
    ])

  }



  return (
    <div>

      <h1>
        LangGraph AI Agent
      </h1>


      <div>

        {
          chat.map((item, index) => (

            <p key={index}>

              <b>
                {item.role}:
              </b>

              {" "}

              {item.content}

            </p>

          ))
        }

      </div>



      <input

        value={message}

        onChange={
          e => setMessage(e.target.value)
        }

        placeholder="Ask something..."

      />


      <button onClick={sendMessage}>
        Send
      </button>


    </div>
  )
}


export default App