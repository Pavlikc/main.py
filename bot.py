# сылка на бота https://discord.com/oauth2/authorize?client_id=1231177142109212682&permissions=8&scope=bot
import discord
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)
y = ['angle', 'tails']
x=''
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('coin'):
        x = random.choice(y)
        await message.channel.send(x)
    else:
        await message.channel.send(message.content)

client.run("MTIzMTE3NzE0MjEwOTIxMjY4Mg.GRjza4.voWFBajAsen2MZLByjCaHIBkAeLAI7S_7AYqa4")
