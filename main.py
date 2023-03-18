# Need to handle char limit for discord messages
# Need to handle number of api calls to chatgpt

import discord
from backend import GptBot
from config import DISCORD_KEY

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bozo_bot = GptBot()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bozo'):
        message.content.split()[0].replace("!bozo","")
        if len(message.content.split()) > 1:
            user_message = message.content[1:]
            await message.channel.send(bozo_bot.get_response(user_message))
            user_message = ""

    if message.content.startswith('!paint'):
        message.content.split()[0].replace("!paint","")
        if len(message.content.split()) > 1:
            user_message = message.content[1:]
            await message.channel.send(bozo_bot.get_response(user_message))
            user_message = ""

client.run(DISCORD_KEY)
