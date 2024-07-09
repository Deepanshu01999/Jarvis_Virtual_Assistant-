# Jarvis_Virtual_Assistant
• Jarvis is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, fetching news.

**FEATURES**

1. Voice Recognition
2. Utilizes the speech_recognition library to listen for and recognize voice commands.
3. Activates upon detecting the wake word "Jarvis."
4. Text-to-Speech
5. Converts text to speech using pyttsx3 for local conversion.
6. Web Browsing.
7. Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.
8. Music Playback
9. Interfaces with a musicLibrary module to play songs via web links.
10. News Fetching
11. Fetches and reads the latest news headlines using NewsAPI.
12. Acts as a general virtual assistant similar to Alexa or Google Assistant.
13. Activates upon detecting the wake word "Jarvis."
14. Text-to-Speech

**WORKFLOW**

1. Initialization
2. Greets the user with "Initializing Jarvis...."
3. Wake Word Detection
4. Listens for the wake word "Jarvis."
5. Acknowledges activation by saying "Ya."
6. Command Processing.
7. Processes commands to determine actions such as opening a website, playing music, fetching news, or generating a response via OpenAI.
8. Speech Output.
9. Provides responses using speak function with either pyttsx3 .
