import discord
from psw import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Hola, como esta tu día!")
    elif message.content.startswith('$psw'):
        await message.channel.send(f"Aquí está tu contraseña {gen_pass(8)}")
    elif message.content.startswith('$que_es_python'):
        await message.channel.send("Python el mejor lenguaje de programación de todos los tiempos.")
    elif message.content.startswith('$chau'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$como_estas'):
        await message.channel.send("bien y tu?")
    elif message.content.startswith('$bien'):
        await message.channel.send("Genial")
    elif message.content.startswith('$genial'):
        await message.channel.send("Que bien")
    else:
        await message.channel.send(message.content)

token = "ingresa tu token"
client.run(token)
