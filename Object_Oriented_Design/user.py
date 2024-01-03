
from message import Message

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.messages = []
        self.displayed_messages = set()

    def send_message(self, content, recipient):
        message = Message(content, self, recipient)
        recipient.receive_message(message)
        self.messages.append(message)

    def receive_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def display_messages(self):
        print(f"\nMessages for {self.username}:")
        for message in self.messages:
            if message not in self.displayed_messages:
                print(message)
                self.displayed_messages.add(message)
