import os
import discord
import json
import requests
from .. import messages, user
from ...model.message import insert_message
import pymongo
import asyncio


def run(message_list):
    keys = json.load(open('keys.json'))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

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
                id = requests.get(url).text
                users_dict[message.author.id] = user.User(message.author.name, id, None, 'Discord')
            
            insert_message(messages.Messages(users_dict[message.author.id], message.content))
            print(messages.Messages(users_dict[message.author.id], message.content))
            
    client.run(TOKEN)