import os
import discord
from dotenv import load_dotenv
import TData

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

td = TData.TData()
stock_list = list()
with open('stocklist', 'r') as f:
    tmp = f.readlines()
for data in tmp:
    stock_list.append(data.rstrip().lower())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '420' or message.content == '69':
        await message.channel.send('nice')
        await message.channel.send('Support slackers: https://github.com/adamsand123/stockbot')
    if message.content.lower() in stock_list:
        for stock in stock_list:
            if message.content == stock:
                await message.channel.send(td.get_value(stock.upper()))


client.run(token)
