

from message import Message

class ChatRoom:
    def __init__(self, participants):
        self.participants = participants
        self.messages = []

    def send_group_message(self, content, sender):
        group_message = Message(content, sender, self)
        for participant in self.participants:
            if participant != sender:
                participant.receive_message(group_message)
        self.messages.append(group_message)

    def get_members(self):
        return [participant.username for participant in self.participants]
