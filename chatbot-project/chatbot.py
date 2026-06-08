# DecodeLabs Project 1 - Rule-Based AI Chatbot

print("=" * 50)
print("🤖 Welcome to DecodeBot AI Assistant")
print("Type 'help' to see commands")
print("Type 'bye' to exit")
print("=" * 50)

name = input("Before we start, what's your name? ").strip()

print(f"\nHello {name}! Nice to meet you. 😊")

while True:
    user_input = input(f"\n{name}: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("🤖 DecodeBot: Hello! How can I help you today?")

    # Personal info
    elif user_input == "who am i":
        print(f"🤖 DecodeBot: You are {name}.")

    # Bot name
    elif user_input == "what is your name":
        print("🤖 DecodeBot: My name is DecodeBot AI Assistant.")

    # Health
    elif user_input == "how are you":
        print("🤖 DecodeBot: I'm doing great! Thanks for asking.")

    # Joke
    elif user_input == "joke":
        print("🤖 DecodeBot: Why do programmers prefer dark mode?")
        print("🤖 DecodeBot: Because light attracts bugs! 😂")

    # Help menu
    elif user_input == "help":
        print("\nAvailable Commands:")
        print("- hi / hello / hey")
        print("- how are you")
        print("- what is your name")
        print("- who am i")
        print("- joke")
        print("- help")
        print("- bye")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print(f"🤖 DecodeBot: Goodbye {name}! Have a great day. 👋")
        break

    # Unknown input
    else:
        print("🤖 DecodeBot: Sorry, I don't understand that command.")