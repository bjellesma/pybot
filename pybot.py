import discord
import os
from dotenv import load_dotenv

load_dotenv()
# get token from store
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# class decorator used for all discord methods
# because asyncio is used under the hood
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # we only want to take action if someone else sent the message
    if message.author != client.user:
        message_string = message.content
        # if the first character is an exclamation, the person is talking to the bot
        if message_string.startswith('!'):
            # strip the first character
            message_content = message_string[1:]
            if message_content == "hello":
                await message.channel.send('Goodbye')

client.run(TOKEN)