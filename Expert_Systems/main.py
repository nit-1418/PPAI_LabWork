from Emotional import EmotionalChatbot



if __name__ == "__main__":
    chatbot = EmotionalChatbot()

    print("Emotional Chatbot: Hi there! How can I help you today? (Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Emotional Chatbot: Goodbye! Take care.")
            break

        response = chatbot.chat(user_input)
        print(f"Emotional Chatbot: {response}")