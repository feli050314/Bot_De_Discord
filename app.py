import discord
from discord.ext import commands
import random 
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

emojis = [
    "😀", "😄", "😁", "😂", "🤣", "😊", "😇", "😉", "😍", "😘",  # Caritas felices
    "😎", "🤩", "🥳", "🤗", "🤔", "😐", "😴", "🤤", "😢", "😭",  # Emociones varias
    "😡", "😱", "😳", "🥶", "🥵", "🤯", "😈", "👻", "💀", "🤖",  # Locuras y sustos
    "🐶", "🐱", "🐭", "🐹", "🐰", "🐻", "🐼", "🐨", "🐸", "🐵",  # Animales
    "🌸", "🌻", "🌲", "🌴", "🍀", "🍁", "🍄", "🌞", "🌈", "⭐",  # Naturaleza
    "🍎", "🍌", "🍉", "🍇", "🍓", "🍔", "🍕", "🍟", "🍩", "🍪",  # Comida
    "⚽", "🏀", "🎮", "🎲", "🎵", "🎤", "🎬", "🎨", "✈️", "🚗",  # Actividades y objetos
    "🎁", "🎉", "💌", "❤️", "💔", "🔥", "💧", "⭐", "🌙", "☀️"   # Cosas lindas y símbolos
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send('Chau!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def emoji(ctx, num = 1):
    for i in range(num):
        respuesta = random.choice(emojis)
        await ctx.send(respuesta)


@bot.command()
async def suma(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def resta(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def adivina(ctx):
    numero_secreto = random.randint(1, 10)
    await ctx.send("Estoy pensando en un número del 1 al 10... ¿Cuál crees que es? 🤔")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    msg = await bot.wait_for("message", check=check)
    respuesta = int(msg.content)
    if respuesta == numero_secreto:
        await ctx.send("🎉 ¡Adivinaste! Eres genial 😎")
    else:
        await ctx.send(f"❌ Nope, el número secreto era **{numero_secreto}**")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def meme(ctx):
    with open('imagenes/meme1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

#Ejercicio # 3  
@bot.command()
async def randomeme(ctx):
    imagenes = os.listdir('imagenes')
    img_name = random.choice(imagenes)
    with open(f'imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command("randomzoro")
async def randomzoro(ctx):
    imagenes_zoro = os.listdir('imagenes_zoro')
    img_name_zoro = random.choice(imagenes_zoro)
    with open(f'imagenes_zoro/{img_name_zoro}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command("medio_ambiente")
async def medio_ambiente(ctx):
    tips = [
        "Reduce, reutiliza y recicla siempre que sea posible ♻️",
        "Usa bolsas reutilizables en lugar de bolsas plásticas 🛍️",
        "Evita comprar botellas desechables; usa botellas o termos reutilizables 🚰",
        "Ahorra energía apagando luces y aparatos cuando no los uses 💡",
        "Desconecta cargadores y electrónicos para evitar el consumo fantasma 🔌",
        "Aprovecha la luz natural durante el día 🌞",
        "Reduce el consumo de agua, por ejemplo, tomando duchas más cortas 🚿",
        "Repara antes de reemplazar: ropa, aparatos, muebles, etc. 🧵",
        "Compra productos locales para reducir la huella de transporte 🛒",
        "Evita el uso de plásticos de un solo uso (cubiertos, vasos, platos) 🥤",
        "Separa correctamente la basura, especialmente orgánicos y reciclables 🚮",
        "Haz compost con restos de comida y hojas (si tienes espacio) 🌱",
        "Utiliza transporte sostenible: caminar, bicicleta, bus o compartir auto 🚶‍♂️🚲",
        "Planta árboles o cuida plantas para mejorar el aire 🌳",
        "Elige productos ecológicos o biodegradables cuando sea posible 🌿",
        "Reduce el consumo de carne, aunque sea algunos días a la semana 🍃",
        "Evita imprimir si no es necesario; usa formatos digitales 🖥️",
        "Cuida el agua cerrando el grifo mientras te cepillas los dientes 🚰",
        "No tires basura en la calle o en la naturaleza 🚯",
        "Participa en limpiezas comunitarias de playas, ríos o parques 🤝"
    ]

    tip = random.choice(tips)
    await ctx.send(tip)

bot.run("ingresa tu token")
