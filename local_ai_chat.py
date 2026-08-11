print("=" * 45)
print("     Shawn's FinTech AI Assistant")
print("=" * 45)
print()

from ollama import chat
from datetime import datetime
from pathlib import Path
WORKSPACE_FOLDER = Path("workspace").resolve()

def is_safe_workspace_file(file_path):
    requested_path = Path(file_path).resolve()
    return (
        requested_path.is_file()
        and requested_path.is_relative_to(WORKSPACE_FOLDER)
    )

def read_workspace_file(file_path):
    if not is_safe_workspace_file(file_path):
         return "Acess denied. The file must be inside the approved workspace folder." 
    return Path(file_path).read_text(encoding="utf-8")

def list_workspace_files():
    if not WORKSPACE_FOLDER.exists():
        return []
    return [
        file.name
        for file in WORKSPACE_FOLDER.iterdir()
        if file.is_file()
    ]
         
def save_conversation(messages):
     if not messages:
          return
     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
     filename = f"conversations/conversation_{timestamp}.txt"
     with open(filename, "w", encoding="utf-8") as file:
          for message in messages:
               role = message["role"].capitalize()
               content = message["content"]
               file.write(f"{role}: {content}\n\n")

     print(f"\nConversation saved as {filename}\n")

if __name__ == "__main__":
    messages = []  
    while True:
        user_question = input("Ask a finance or blockchain question: ").strip()
        if  not user_question:
            print("\nPlease enter a question before pressing Enter.\n")
            continue
        if  user_question.lower() == "help":
            print("\nAvailable commands:")
            print("  help  - Show available commands")
            print("  files - Show approved workspace files")
            print("  read <filename> - Read an approved workspace file")
            print("  analyze <filename> - Analyze an approved workspace document")
            print("  clear - Clear the conversation memeory")
            print("  status - Shos AI Assistant system status")
            print("  exit  - Close the AI Assistant\n")
            continue
        if  user_question.lower() == "status":
            print("\nAI Assistant System Status:")
            print("  Core Assistant: ONLINE")
            print(f"  Workspace: {'READY' if WORKSPACE_FOLDER.exists() else 'NOT FOUND'}")
            print(f"  Approved Files: {len(list_workspace_files())}")
            print(f"  Conversation Memory: {len(messages)} messages")
            print(f" Safety Mode: APPROVED WORKSPACE ONLY\n")
            continue
        if  user_question.lower() == "files":
             files = list_workspace_files()
             if files:
                 print("\nWorkspace files:")
                 for file in files:
                     print(f"  - {file}")
             else:
                 print("nNo files found in the workspace.")
        if user_question.lower().startswith("read "):
            filename = user_question[5:].strip()
            file_path = WORKSPACE_FOLDER / filename
            try:
                content = read_workspace_file(file_path)
                print(f"\nContents of {filename}:\n")
                print(content)
                print()
            except Exception as error:
                print(f"\nUnable to read file: {error}\n")
            continue
        if user_question.lower().startswith("analyze "):
            filename = user_question[8:].strip()
            file_path = WORKSPACE_FOLDER / filename
            try:
                content = read_workspace_file(file_path)
                user_question = (
                    f"Analyze the following document named '{filename}'. "
                    "Provide a clear summary, identify the main ideas, "
                    "highlight important details, and explain the material "
                    f"in plain language.\n{content}"
                ) 
            except Exception as error:
                print(f"\nUnable to analyze file: {error}\n")
                continue
        if  user_question.lower() == "clear":
            messages.clear()
            print("\nConversation memory cleared.\n")
            continue
        if  user_question.lower() =="exit":
            save_conversation(messages)
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