from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

class EmotionClassifier:
    def __init__(self):

        training_data = training_data = [
            ('I feel happy', 'happy'),
            ('I am happy today', 'happy'),
            ('I feel fantastic', 'happy'),
            ('This is great news', 'happy'),
            ('I can\'t stop smiling', 'happy'),
            ('I feel joyful', 'happy'),
            ("I'm on cloud nine", 'happy'),
            ("I'm in a good mood", 'happy'),
            ('I feel sad', 'sad'),
            ('I had a tough day', 'sad'),
            ('Feeling down right now', 'sad'),
            ("I'm feeling a bit blue", 'sad'),
            ('This is really upsetting', 'sad'),
            ('I feel melancholic', 'sad'),
            ("I'm heartbroken", 'sad'),
            ("I'm disappointed", 'sad'),
            ("I'm angry", 'angry'),
            ('This is infuriating', 'angry'),
            ('I can\'t tolerate this', 'angry'),
            ('Feeling really annoyed', 'angry'),
            ("I'm frustrated", 'angry'),
            ("I'm enraged", 'angry'),
            ("I'm furious", 'angry'),
            ("I'm surprised", 'surprise'),
            ('This is unexpected', 'surprise'),
            ("I can't believe it!", 'surprise'),
            ('Surprise, I got you a gift!', 'surprise'),
            ("I'm astonished", 'surprise'),
            ('This is a pleasant surprise', 'surprise'),
            ("I'm taken aback", 'surprise'),
            ('Feeling neutral', 'neutral'),
            ("I don't have strong emotions right now", 'neutral'),
            ('Just a normal day', 'neutral'),
            ('Not particularly happy or sad', 'neutral'),
            ("I'm indifferent", 'neutral'),
            ('I feel neutral', 'neutral'),
            ("I'm neither happy nor sad", 'neutral'),
            ("I'm in a neutral state", 'neutral'),
            ("Teacher praised me", 'happy')
        ]

        #  machine learning model
        self.model = make_pipeline(CountVectorizer(), RandomForestClassifier())
        texts, emotions = zip(*training_data)
        self.model.fit(texts, emotions)

    def predict_emotion(self, text):
        # This Predicts emotion using the trained model
        predicted_emotion = self.model.predict([text])[0]
        return predicted_emotion

    def evaluate_model(self):
        #  we are here training data is seperated into texts and emotions
        texts, true_emotions = zip(*self.training_data)

        # Predicts emotions on the training data
        predicted_emotions = self.model.predict(texts)
