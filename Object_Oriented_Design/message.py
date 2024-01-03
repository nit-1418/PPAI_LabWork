from datetime import datetime

class Message:
    def __init__(self, content, sender, recipient):
        self.content = content
        self.sender = sender
        self.recipient = recipient
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}: {self.content}"
