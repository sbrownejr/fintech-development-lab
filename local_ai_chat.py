print("=" * 45)
print("     Shawn's FinTech AI Assistant")
print("=" * 45)
print()

from ollama import chat


messages = []  
while True:
    user_question = input("Ask a finance or blockchain question: ").strip()
    if  not user_question:
         print("\nPlease enter a question before pressing Enter.\n")
         continue
    if  user_question.lower() == "help":
         print("\nAvailable commands:")
         print("  help  - Show available commands")
         print("  clear - Clear the conversation memeory")
         print("  exit  - Close the AI Assistant\n")
         continue
    if  user_question.lower() == "clear":
         messages.clear()
         print("\nConversation memory cleared.\n")
         continue
    if  user_question.lower() =="exit":
         print("\nThanks for using Shawn's FinTech AI Assistant!")
         break
    
    messages.append({
        "role": "user",
        "content": user_question,
    })
    print("\nAI is thinking...\n")
    response = chat(
        model="gemma3:4b",
        messages=messages,
    )

    print(response["message"]["content"])
    messages.append({
         "role": "assistant",
         "content": response["message"]["content"],
    })     