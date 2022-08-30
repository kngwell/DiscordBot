import os
import discord
from discord.ext import commands

my_secret = os.environ['TOKEN']
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    guilds = [guild async for guild in client.fetch_guilds(limit=150)]
    print(f'{guilds}')
    await client.load_extension('messages')
    await client.load_extension('reactions')

client.run(my_secret)