from .login import db

def insert_message(user):
    db.author.insert_one({'user': user.id, 'name': user.name,'ip': user.ip, 'type': user.type})
