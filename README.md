--------------------------------------------------- WhatsApp Chatbot -----------------------------------------------------

This WhatsApp chatbot automates responses based on chat history, simulating a conversational agent named Arjun K. The bot is designed to operate on WhatsApp Web by interacting with the screen using pyautogui and processing messages with the Groq API.

Features
Automates response on WhatsApp Web.
Customizes responses based on sender's identity and chat content.
Detects if a particular sender sent the last message.
Supports conversational replies in both Hindi and English.

Code Overview
main.py - Runs the bot, captures cursor positions, and interacts with the chat interface.
groq_module.py - Handles the chatbot's response generation with the Groq API.

Important Notes
The bot operates on fixed screen coordinates, so adjustments might be necessary for different screen resolutions.
The bot simulates user actions (clicks, copy/paste, etc.), which may cause unexpected behavior if other applications interfere.

Contributing
Feel free to submit issues or pull requests for enhancements or bug fixes.

