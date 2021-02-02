import os
import discord
from dotenv import load_dotenv
import TData

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

td = TData.TData()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '420' or message.content == '69':
        await message.channel.send('nice')
    if message.content == 'rip':
        print(td.get_gme())


client.run(token)
