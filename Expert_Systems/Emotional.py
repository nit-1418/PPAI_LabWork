from chatbot_model import EmotionClassifier
import random

class EmotionalChatbot:
    def __init__(self):
        self.emotion_classifier = EmotionClassifier()
        self.context = {}  ##context for each emotion

    def chat(self, user_input):
        #  emotion prediction using the classifier
        predicted_emotion = self.emotion_classifier.predict_emotion(user_input)

        # Process user input and generate a context-wise response, okay
        response = self.process_user_input(predicted_emotion, user_input)
        return response

    def process_user_input(self, emotion, user_input):
        # Update context based on the user's response
        self.context[emotion] = user_input

        if emotion in self.context:
            print(f"Emotional Chatbot: It seems you're feeling {emotion}.")
            print(f"Emotional Chatbot: {self.generate_response(emotion, user_input)}")
            print("Emotional Chatbot: Is there anything specific you'd like to talk about?")
            user_response = input("You: ")
            print("Emotional Chatbot: Thank you for sharing. If you need more support, feel free to reach out.")
        else:
            print("I am here to chat with you :)")

    # Generating  context-wise response
    def generate_response(self, emotion, user_input):

        if emotion == 'happy':
            return self.generate_happy_response()
        elif emotion == 'sad':
            return self.generate_sad_response()
        elif emotion == 'angry':
            return self.generate_angry_response()
        elif emotion == 'surprise':
            return self.generate_surprise_response()
        elif emotion == 'neutral':
            return self.generate_neutral_response()
        else:
            return self.generate_default_response()

    # Happy responses
    def generate_happy_response(self):
        responses = [
            "I'm glad to hear that you're feeling happy!",
            "That's wonderful! What brought you joy today?",
            "Happiness is contagious! Anything special making you happy?",
            "Fantastic! Let's celebrate the positive vibes. What's making you happy?",
            "It's great to start the day with a smile. What's making you feel happy right now?"
        ]
        return random.choice(responses)

    # Sad responses
    def generate_sad_response(self):
        responses = [
            "I'm sorry to hear that you're feeling sad. How can I help?",
            "It's okay to feel sad sometimes. Would you like to talk about what's on your mind?",
            "Feeling sad is a natural emotion. Let's discuss it together.",
            "I empathize with your sadness. Is there something specific bothering you?",
            "Sending virtual hugs your way. If you want to share, I'm here to listen."
        ]
        return random.choice(responses)

    # Angry responses
    def generate_angry_response(self):
        responses = [
            "It sounds like you're upset. Let's talk about it.",
            "I understand anger can be overwhelming. Share your feelings with me.",
            "Feeling angry is normal. What triggered your anger?",
            "Take a deep breath. If you're comfortable, tell me more about what's bothering you.",
            "I'm here to help you navigate through your anger. What's on your mind?"
        ]
        return random.choice(responses)

    # Surprise responses
    def generate_surprise_response(self):
        responses = [
            "Wow! That's surprising. Tell me more.",
            "I didn't see that coming! What's the story behind the surprise?",
            "Unexpected twists can be exciting. Share more about what surprised you.",
            "Surprises can be both thrilling and mysterious. Want to talk about it?",
            "What a pleasant surprise! Let's delve into the details."
        ]
        return random.choice(responses)

    # Neutral responses
    def generate_neutral_response(self):
        responses = [
            "I'm here to chat. How are you feeling?",
            "Neutral feelings are valid too. Is there anything specific on your mind?",
            "Sometimes being in a neutral state is a moment of calmness. What's going on?",
            "No strong emotions? That's okay. We can talk about anything you'd like.",
            "Whether happy, sad, or neutral, I'm here for you. What would you like to discuss?"
        ]
        return random.choice(responses)

    # say normal responses
    def generate_default_response(self):
        responses = [
            "I'm here to chat. How are you feeling?",
            "I didn't catch that. Could you please rephrase or share more details?",
            "Let's continue the conversation. Is there a specific topic you'd like to discuss?",
            "I'm here for you. Feel free to express your thoughts, and we can talk about anything.",
            "It seems like we're on different wavelengths. Can you provide more context or ask a specific question?"
        ]
        return random.choice(responses)



