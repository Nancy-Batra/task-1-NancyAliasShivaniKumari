print("Welcome to the Rule-Based Chatbot!")

greetings = ["hello", "hi", "hey"]
goodbye = ["bye", "goodbye", "see you"]
thanks = ["thanks", "thank you"]

responses = {
    "greeting": "Hi there! How can I help you?",
    "thanks": "You're welcome!",
    "goodbye": "Goodbye! Have a nice day.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "help": "You can say hello, ask my name, ask how I am, or type exit."
}

while True:
    user_input = input("\n What’s on the agenda today?: ").lower().strip()

    if user_input == "exit":
        print("Goodbye!")
        break

    elif user_input in greetings:
        print(responses["greeting"])

    elif user_input in thanks:
        print(responses["thanks"])

    elif user_input in goodbye:
        print(responses["goodbye"])

    elif user_input in responses:
        print(responses[user_input])

    elif "weather" in user_input:
        print("Sorry, I cannot check live weather yet.")

    elif "your age" in user_input:
        print("I don't have an age. I was created using Python!")

    else:
        print("I don't understand that. Type 'help' to see available commands.")