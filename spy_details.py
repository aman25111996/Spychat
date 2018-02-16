from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('agent rouge', 'Mr.', 27, 4.9)
friend_two = Spy('pink panther', 'Ms.', 21, 4.79)
friend_three = Spy('dexter', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
