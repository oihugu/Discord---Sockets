import os
import discord
import json
import requests
from .. import messages, user

def run(message_list):
    keys = json.load(open('keys.json'))

    TOKEN = keys['discord']

    client = discord.Client()

    users_dict = {}

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('!help'):
            await message.channel.send('Só estou ouvindo')
        else:
            if message.author.id not in users_dict:
                url = os.environ['APP_URL'] + '/generate_id'
                id = requests.get(url)
                users_dict[message.author.id] = user.User(message.author.name, id, None, 'Discord')
            
            message_list.append(messages.Messages(users_dict[message.author.id], message.content))
            print(messages.Messages(users_dict[message.author.id], message.content))
            
    client.run(TOKEN)