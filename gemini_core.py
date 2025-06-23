# gemini_core.py

import os
import google.generativeai as genai

# --- API and Model Setup ---
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Gemini Core Engine Initialized Successfully.")
except Exception as e:
    print(f"🚨 CRITICAL ERROR: Could not configure Gemini Core. Details: {e}")
    model = None # Set model to None if initialization fails

def start_new_chat_session(personality_prompt):
    """Starts a new chat session with the given personality as the system instruction."""
    if not model:
        raise ConnectionError("Gemini model is not initialized. Check API key.")
        
    # Using 'parts' to define the role of the first message
    return model.start_chat(history=[
        {
            "role": "user",
            "parts": ["(SYSTEM INSTRUCTION: From now on, you MUST follow this instruction: " + personality_prompt + ")"]
        },
        {
            "role": "model",
            "parts": ["Understood. I will act according to that personality. I am ready."]
        }
    ])