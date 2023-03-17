# This example requires the 'message_content' intent.

import discord
from backend import Chatbot
from config import DISCORD_KEY

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
chatbot = Chatbot()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bozo'):
        cmd = message.content.split()[0].replace("!bozo","")
        if len(message.content.split()) > 1:
            user_message = message.content[1:]
            await message.channel.send(chatbot.get_response(user_message))
            user_message = ""

client.run(DISCORD_KEY)
