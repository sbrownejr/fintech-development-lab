from ollama import chat

user_question = input("Ask a finance or blockchain question: ")

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": user_question,
        }
    ],
)

print(response["message"]["content"])