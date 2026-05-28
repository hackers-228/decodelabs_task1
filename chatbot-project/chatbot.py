# Rule-Based AI Chatbot

print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
   
    user_input = input("You: ").lower().strip()

    # Greeting responses
    if user_input == "hello" or user_input == "hi":
        print("🤖 ChatBot: Hi there!")

    elif user_input == "how are you":
        print("🤖 ChatBot: I'm fine! How can I help you?")

    elif user_input == "what is your name":
        print("🤖 ChatBot: I am a Rule-Based AI Chatbot.")

    elif user_input == "help":
        print("🤖 ChatBot: You can say hello, ask my name, or type bye to exit.")

    # Exit condition
    elif user_input == "bye" or user_input == "exit":
        print("🤖 ChatBot: Goodbye! Have a great day.")
        break

    # Default response
    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")