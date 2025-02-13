import os
import requests

# Set your Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Load from environment variable for security
GROQ_API_URL = "https://api.groq.com/v1/chat/completions"

def chat_with_groq():
    print("Welcome to the Groq Chatbot! Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Exiting... Goodbye!")
            break

        response = get_groq_response(user_input)
        print(f"Groq: {response}")

def get_groq_response(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",  # Change to appropriate Groq model if needed
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(GROQ_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to get a response from Groq."

if __name__ == "__main__":
    chat_with_groq()
