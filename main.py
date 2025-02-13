import os
import requests

# Set your Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Load from environment variable for security
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

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
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY is missing. Please set it in your environment."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",  # Change to appropriate Groq model if needed
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        print(f"🔍 DEBUG: Status Code: {response.status_code}")
        print(f"🔍 DEBUG: Response Text: {response.text}")
        
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response content.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed - {e}"

if __name__ == "__main__":
    chat_with_groq()
