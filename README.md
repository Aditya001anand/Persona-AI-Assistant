# Persona: An AI Assistant Web Application

## 1. Project Objective

[cite_start]This project is an AI-powered web application that allows users to engage in dynamic conversations with multiple AI personalities.  [cite_start]It showcases skills in crafting effective prompts to drive varied and context-aware responses from the Gemini AI model. 

## 2. Features

* [cite_start]**Dynamic Personalities:** Users can choose from four unique AI personalities, each with its own theme, tone, and style. 
    * Helpful Assistant
    * Sarcastic Robot
    * Shakespearean Poet
    * Timid Nerd
* **Interactive Chat Interface:** A modern, responsive chat interface with features like avatars, themed backgrounds, dynamic colors, code syntax highlighting, and a copy-to-clipboard button.
* [cite_start]**Persistent Conversations:** The application maintains conversation history within a session, allowing for natural, follow-up questions. 
* **"About the Project" Modal:** An informational pop-up provides details about the project and its technology.

## 3. How to Set Up and Run the Project

**Prerequisites:**
* Python 3.x
* A Google Gemini API Key

**Setup Instructions:**
1.  Clone or download the project files.
2.  Navigate to the project directory in your terminal.
3.  Install the required Python libraries by running: `pip install -r requirements.txt`
4.  Create a file named `.env` in the main project directory.
5.  Add your Google Gemini API key to the `.env` file in the following format:
    `GOOGLE_API_KEY="YOUR_API_KEY_HERE"`
6.  Run the web application using the command: `flask run`
7.  Open your web browser and go to `http://127.0.0.1:5000`.

## 4. Prompt Design

[cite_start]This project utilizes a flexible prompt framework where a base system prompt defines the AI's core personality.  For example, the prompt for the "Sarcastic Robot" is:
> "You are a sarcastic robot. Your answers should be factually correct, but delivered with a dry, sarcastic wit. You reluctantly provide help."

[cite_start]This initial prompt guides the AI's tone and style for the entire conversation, demonstrating prompt-driven context control.