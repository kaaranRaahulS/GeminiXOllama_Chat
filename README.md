# GeminiXOllama_Chat
A fun experimental project that creates a live conversation between two large language models with opposite personalities:

Ollama (LLaMA 3.2) → overly polite, calm, and agreeable

Google Gemini → snarky, argumentative, and challenging

The project demonstrates how system prompts and conversation history influence LLM behavior.

**Prerequisites**

1. Python 3.9+

2. Ollama installed locally

3. Google Gemini API key

**Setup & Installation**
1. Install Ollama Locally
  https://ollama.com
2. Pull the required model:
   ollama pull llama3.2
3. clone the Repository
4. create .env file => GOOGLE_API_KEY=your_gemini_api_key_here
5. Install Dependencies => pip install ollama google-generativeai python-dotenv
6. python <name_of_the_file>.py

**Purpose:** 

Built purely for fun and experimentation, this project explores:

* Prompt engineering

* Multi-model orchestration

* Personality control in LLM conversations
