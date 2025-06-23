# app.py

# --- ADD THESE TWO LINES AT THE VERY TOP ---
from dotenv import load_dotenv
load_dotenv()
# ------------------------------------------

from flask import Flask, render_template, request, jsonify, session
import os
from gemini_core import model # Import the model from our other file

# ... the rest of your app.py file remains the same

from flask import Flask, render_template, request, jsonify, session
import os
from gemini_core import model # Import the model from our other file

# Initialize the Flask application
app = Flask(__name__)
# A secret key is needed to use sessions, which store data between requests.
app.secret_key = os.urandom(24) 

# In app.py

# In app.py

PERSONALITIES = {
    'assistant': {
        "name": "Helpful Assistant",
        "prompt": "You are a helpful and friendly AI assistant. Be clear, concise, and polite.",
        "background_image": "images/assistant_bg.png",
        "theme_color": "#007BFF",
        "avatar_image": "avatars/assistant_avatar.png" # <-- ADDED
    },
    'robot': {
        "name": "Sarcastic Robot",
        "prompt": "You are a sarcastic robot. Your answers should be factually correct, but delivered with a dry, sarcastic wit. You reluctantly provide help.",
        "background_image": "images/robot_bg.png",
        "theme_color": "#FF0055",
        "avatar_image": "avatars/robot_avatar.png" # <-- ADDED
    },
    'poet': {
        "name": "Shakespearean Poet",
        "prompt": "Thou art a poet from Shakespearean times...",
        "background_image": "images/poet_bg.png",
        "theme_color": "#4a443a",
        "avatar_image": "avatars/poet_avatar.png" # <-- ADDED
    },
    'nerd': {
        "name": "Timid Nerd",
        "prompt": "You are a shy and timid assistant...",
        "background_image": "images/nerd_bg.png",
        "theme_color": "#5c9aff",
        "avatar_image": "avatars/nerd_avatar.png" # <-- ADDED
    }
}

@app.route('/')
def homepage():
    """Renders the homepage and passes personality data to it."""
    return render_template('index.html', personalities=PERSONALITIES)
# --- NEW: Route for the Chat Page ---
@app.route('/chat')
def chat_page():
    """Renders the main chat interface."""
    # Get the chosen personality from the URL parameter (?personality=...)
    personality_key = request.args.get('personality', 'assistant') # Default to assistant
    personality = PERSONALITIES.get(personality_key, PERSONALITIES['assistant'])

    # Start a new chat session and store its history in the user's session
    # For web apps, we manage history this way.
    session['chat_history'] = [
        {"role": "user", "parts": ["(SYSTEM INSTRUCTION: " + personality['prompt'] + ")"]},
        {"role": "model", "parts": ["Understood. I will act according to that personality."]}
    ]
    
    # In the chat_page function in app.py

    return render_template('chat.html', 
                           personality_name=personality['name'], 
                           background_image=personality['background_image'],
                           theme_color=personality['theme_color'],
                           avatar_image=personality['avatar_image']) # <-- ADD THIS LINE
# In app.py, use this new version of the function.

@app.route('/get_response', methods=['POST'])
def get_response():
    """Handles the chat message and gets a response from the AI."""
    if not model:
        return jsonify({'error': 'The AI model is not initialized. Make sure the API key is set correctly before starting the server.'}), 500

    try:
        data = request.json
        user_message = data['message']
        
        # Retrieve the conversation history from the user's session
        history = session.get('chat_history', [])
        
        # Add the new user message to the history
        history.append({"role": "user", "parts": [user_message]})

        # Use the model to generate content based on the entire history
        # This is a simpler and more stateless way to get a response
        response = model.generate_content(history)
        
        ai_message = response.text
        
        # Add the AI's response to our history
        history.append({"role": "model", "parts": [ai_message]})
        
        # Save the updated history back to the session
        session['chat_history'] = history

        return jsonify({'response': ai_message})

    except Exception as e:
        # Log the error to the terminal for debugging
        print(f"An error occurred in /get_response: {e}")
        return jsonify({'error': str(e)}), 500

# In app.py

# --- NEW: Route for Submitting Feedback ---
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """Logs user feedback to a file."""
    data = request.json
    try:
        with open("feedback_log.txt", "a", encoding="utf-8") as f:
            f.write("--------------------------------\n")
            f.write(f"MESSAGE:\n{data['message']}\n\n")
            f.write(f"FEEDBACK: {data['feedback']}\n")
            f.write("--------------------------------\n\n")
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error writing to feedback log: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)