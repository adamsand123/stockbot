import os
import discord
from dotenv import load_dotenv
from TData import TData

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()
summary = ['sum', 'summary']
td = TData()

stock_list = list()
with open('stocklist', 'r') as f:
    tmp = f.readlines()
for data in tmp:
    stock_list.append(data.rstrip().lower())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '420' in message.content or '69' in message.content:
        await message.channel.send(f'nice {message.author}')

    commands = message.content.lower().split()
    if commands[0] in stock_list:
        if str(message.author) == 'Kaztiell#0716':
            await message.channel.send('https://www.swish.nu/ :eyes:')
        elif len(commands) == 2:
            if commands[1].lower() in summary:
                await message.channel.send(td.get_last3(commands[0], commands[1]))
                return
            meta = td.get_meta(commands[0], commands[1])
            last3 = td.get_last3(commands[0], commands[1])
        elif len(commands) == 3 and commands[2] in ['sum', 'summary']:
            await message.channel.send(td.get_last3(commands[0], commands[1], commands[2]))
            return
        else:
            meta = td.get_meta(commands[0])
            last3 = td.get_last3(commands[0])
        if 'Usage:' in meta:
            await message.channel.send(meta)
            return
        await message.channel.send(meta + "\n" + last3)
        #await message.channel.send('https://github.com/adamsand123/stockbot :eyes:')

client.run(token)
