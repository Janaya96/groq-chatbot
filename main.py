import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor

class Subject(BaseModel):
    title: str
    details: List[str] = Field(..., description="A list of details about the topic")

def get_topic_input():
    return input("Enter a topic to explore (or 'quit' to stop): ")

def execute_query(topic):
    client_instance = Groq(
        api_key=os.environ.get(
            os.environ.get("GROQ_API_KEY"),
        ),
    )

    client_instance = instructor.from_groq(client_instance, mode=instructor.Mode.TOOLS)

    response = client_instance.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "user",
                "content": f"Provide information about {topic}",
            }
        ],
        response_model=Subject,
    )
    print(response.model_dump_json(indent=2))

if __name__ == "__main__":
    while True:
        topic_input = get_topic_input()
        if topic_input.lower() == 'quit':
            break
        execute_query(topic_input)
