import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '420' or '69' in message.content():
        await message.channel.send('nice')


client.run(token)
