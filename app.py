import discord
import random
from discord.ext import commands

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

bot.run("ingresa tu token")
