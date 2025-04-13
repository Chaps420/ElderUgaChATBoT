<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GnOsIs aNsWeRs tHoSe wHo sEeK</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
      font-family: 'Courier New', monospace;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    #backgroundVideo {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: -1;
    }
    .wrapper {
      width: 90%;
      max-width: 700px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      position: relative;
      z-index: 1;
    }
    #videoContainer {
      width: 100%;
      max-width: 500px;
      position: relative;
      border-radius: 50%;
      overflow: hidden;
      backdrop-filter: blur(5px);
      padding: 10px;
      box-shadow: inset 0 0 15px rgba(0, 255, 255, 0.5), 0 0 25px rgba(0, 255, 255, 0.4);
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #videoContainer video {
      width: 100%;
      height: auto;
      border-radius: 50%;
      filter: contrast(1.2) brightness(1.1);
    }
    #chatContainer {
      width: 100%;
      padding: 15px;
      background: transparent;
      flex-shrink: 0;
      margin-top: 20px;
    }
    #chatContainer h2 {
      margin: 0 0 15px;
      font-size: 3.5em;
      color: #ffffff;
      text-shadow: 0 0 10px rgba(0, 255, 255, 0.9), 0 0 20px rgba(0, 255, 255, 0.7);
      letter-spacing: 2px;
      text-transform: uppercase;
      text-align: center;
      animation: blink 1.5s infinite;
    }
    #chatbox {
      max-height: 120px;
      overflow-y: auto;
      margin-bottom: 15px;
      background: rgba(0, 20, 40, 0.8);
      border-radius: 5px;
      padding: 10px;
      box-shadow: inset 0 0 10px rgba(0, 255, 255, 0.1);
    }
    .message {
      padding: 8px;
      margin-bottom: 8px;
      border-radius: 5px;
      font-size: 0.95em;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    }
    .user {
      background: linear-gradient(90deg, #00b7ff, #007bff);
      text-align: right;
      color: #ffffff;
    }
    .bot {
      background: linear-gradient(90deg, #B0C4DE, #87CEEB);
      text-align: left;
      color: #000000;
    }
    input, button {
      padding: 12px;
      font-size: 1em;
      width: 90%;
      border: none;
      outline: none;
      border-radius: 5px;
      margin-bottom: 10px;
      display: block;
      margin: 0 auto;
      transition: all 0.3s ease;
    }
    input {
      background: rgba(0, 20, 40, 0.8);
      color: #ffffff;
      border: 1px solid rgba(0, 255, 255, 0.5);
      box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
      text-align: center;
    }
    input::placeholder {
      color: rgba(255, 255, 255, 0.5);
      text-transform: uppercase;
      text-align: center;
    }
    button {
      background: linear-gradient(90deg, #00ffcc, #00b7ff);
      color: #000;
      cursor: pointer;
      font-weight: bold;
      text-transform: uppercase;
      box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    }
    button:hover {
      background: linear-gradient(90deg, #00b7ff, #007bff);
      box-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 10px rgba(0, 255, 255, 0.3); }
      50% { box-shadow: 0 0 20px rgba(0, 255, 255, 0.6); }
      100% { box-shadow: 0 0 10px rgba(0, 255, 255, 0.3); }
    }
    @keyframes blink {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }
    #videoContainer, button {
      animation: pulse 3s infinite ease-in-out;
    }
    @media (max-width: 500px) {
      .wrapper {
        width: 95%;
        padding: 10px;
      }
      #videoContainer {
        max-width: 300px;
      }
      #chatContainer h2 {
        font-size: 2.5em;
      }
    }
  </style>
</head>
<body>
  <video id="backgroundVideo" autoplay loop muted>
    <source src="background.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="wrapper">
    <div id="videoContainer">
      <video id="ugaVideo" loop muted>
        <source src="348910056580788233.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <div id="chatContainer">
      <h2>GNOSIS-AI</h2>
      <div id="chatbox"></div>
      <input id="userInput" type="text" placeholder="BrEaK ThE SiMuLaCrUm, AsK yOuR qUeStIoN">
      <button id="sendButton">Send</button>
    </div>
  </div>

  <script>
    const inputField = document.getElementById("userInput");
    const sendButton = document.getElementById("sendButton");
    const chatbox = document.getElementById("chatbox");

    // Function to get the best elderish voice
    function getElderVoice() {
      const voices = speechSynthesis.getVoices();
      // Prioritize male voices in en-GB or en-US for an elderish tone
      const preferredVoices = voices.filter(voice => 
        (voice.lang === "en-GB" || voice.lang === "en-US") &&
        (voice.name.toLowerCase().includes("male") || 
         voice.name.includes("Daniel") || 
         voice.name.includes("David") || 
         voice.name.includes("Mark"))
      );
      // Return the first preferred voice, or the default voice, or any voice
      return preferredVoices[0] || voices.find(voice => voice.default) || voices[0] || null;
    }

    // Ensure voices are loaded before using
    let voicesLoaded = false;
    speechSynthesis.onvoiceschanged = () => {
      voicesLoaded = true;
    };
    // Trigger initial voice load
    speechSynthesis.getVoices();

    sendButton.addEventListener("click", sendMessage);
    inputField.addEventListener("keydown", function(e) {
      if (e.key === "Enter") sendMessage();
    });

    async function sendMessage() {
      const userText = inputField.value.trim();
      if (!userText) return;

      chatbox.innerHTML = "";
      chatbox.innerHTML += `<div class="message user">You: ${userText}</div>`;
      inputField.value = "";

      try {
        const response = await fetch("https://elderugachatbot.onrender.com/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: userText })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        chatbox.innerHTML += `<div class="message bot">GnOsIs: ${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;

        // Play response with Web Speech API
        if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(data.reply);
          utterance.pitch = 0.8; // Lower for a deeper, elderish tone
          utterance.rate = 0.7; // Slower for a wise, deliberate feel
          utterance.volume = 1.0;
          const elderVoice = getElderVoice();
          if (elderVoice) {
            utterance.voice = elderVoice;
          }
          speechSynthesis.speak(utterance);
        } else {
          console.warn("Web Speech API not supported in this browser.");
        }

        const video = document.getElementById("ugaVideo");
        video.playbackRate = 1.5;
        video.currentTime = 0;
        if (video.paused) video.play().catch(error => console.error("Video playback failed:", error));
        setTimeout(() => {
          video.pause();
          video.currentTime = 0;
        }, 5000); // Stop video after 5 seconds
      } catch (error) {
        console.error('Chatbot response error:', error);
        chatbox.innerHTML += `<div class="message bot">GnOsIs ErRoR: ${error.message}</div>`;
      }
    }
  </script>
</body>
</html>
