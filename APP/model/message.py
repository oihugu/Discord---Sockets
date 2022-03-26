from ..control import Messages
from .login import db

def insert_message(message):
    db.messages.insert_one({'author': message.author.id, 'content': message.content, 'time' : message.time})

def get_message_list():
    message_list = []
    for message in db.messages.find():
        message_list.append(Messages(message['author'], message['content'], message['time']))
    return message_list
