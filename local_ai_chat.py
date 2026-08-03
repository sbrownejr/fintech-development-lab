print("=" * 45)
print("     Shawn's FinTech AI Assistant")
print("=" * 45)
print()

from ollama import chat


messages = []  
while True:
    user_question = input("Ask a finance or blockchain question: ")

    if  user_question.lower() == "exit":
         print("\nThanks for using Shawn's FinTech AI Assistant!")
         break

    response = chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": user_question,
            },
        ],
    )

    print(response["message"]["content"])