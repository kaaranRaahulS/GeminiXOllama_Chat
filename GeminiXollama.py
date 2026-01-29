import os 
import ollama
from google import genai
from dotenv import load_dotenv

MODEL = "llama3.2"
gemini_model = "gemini-3-flash-preview"

load_dotenv(override = True)

gemini_system_message = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

ollama_system_message = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

def chat_gemini():
    client = genai.Client()
    
    # Build conversation history using Gemini's Content format
    conversation = []
    for ollama_msg, gemini_msg in zip(ollama_messages, gemini_messages):
        conversation.append(genai.types.Content(role='user', parts=[genai.types.Part(text=ollama_msg)]))
        conversation.append(genai.types.Content(role='model', parts=[genai.types.Part(text=gemini_msg)]))
    
    # Only add if there's an unpaired message
    if len(ollama_messages) > len(gemini_messages):
        conversation.append(genai.types.Content(role='user', parts=[genai.types.Part(text=ollama_messages[-1])]))

    response = client.models.generate_content(
        model= gemini_model,
        contents=conversation,
        config=genai.types.GenerateContentConfig(
            system_instruction=gemini_system_message
        )
    )
    return response.text

def chat_ollama():
    message =  [{'role' : 'system', 'content': ollama_system_message}]
    for ollama_msg, gemini_msg in zip(ollama_messages, gemini_messages):
        message.append({'role': 'user', 'content': gemini_msg})
        message.append({'role': 'assistant', 'content': ollama_msg})
    response = ollama.chat(model = MODEL, messages = message)
    return (response['message']['content'])

ollama_messages = ["Hi there"]
gemini_messages = ["Hi"]

print(f"Ollama:\n{ollama_messages[0]}\n")
print(f"Gemini:\n{gemini_messages[0]}\n")

for i in range(5):
    # Call Ollama to generate the next message
    ollama_next = chat_ollama()  
    print(f"Ollama:\n{ollama_next}\n")
    ollama_messages.append(ollama_next)
    
    # Call Gemini to generate the next message
    gemini_next = chat_gemini()  
    print(f"Gemini:\n{gemini_next}\n")
    gemini_messages.append(gemini_next)
