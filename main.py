# Need to handle char limit for discord messages
# Need to handle number of api calls to chatgpt
# Create a cooldown command that checks how long it's been until 
# you can use bozo bot again

import discord
from backend import Bozobot, RestrictCommand
from config import DISCORD_KEY

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bozo_bot = Bozobot()
num_calls = RestrictCommand()



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if num_calls.retrieve_calls() < 1:
        if message.content.startswith('!bozo'):
            message.content.split()[0].replace("!bozo","")
            if len(message.content.split()) > 1:
                user_message = message.content[6:]
                await message.channel.send(bozo_bot.get_response(user_message))
                await message.channel.send(f"\nPrompt: {user_message}")
                user_message = ""
                num_calls.update_calls()

        if message.content.startswith('!paint'):
            message.content.split()[0].replace("!paint"," ")
            if len(message.content.split()) > 1:
                user_message = message.content[7:]
                await message.channel.send(bozo_bot.get_prompt(user_message))
                await message.channel.send(f"\nPrompt: {user_message}")
                user_message = ""
                num_calls.update_calls()
    else:
        print("SUCKS TO SUCK")

client.run(DISCORD_KEY)
