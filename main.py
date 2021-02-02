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
        await message.channel.send('Support slackers: https://github.com/adamsand123/stockbot')
    if message.content == 'gme':
        await message.channel.send(td.get_value('GME'))
        await message.channel.send('Support slackers: https://github.com/adamsand123/stockbot')
    if message.content == 'amc':
        await message.channel.send(td.get_value('AMC'))
        await message.channel.send('Support slackers: https://github.com/adamsand123/stockbot')


client.run(token)
