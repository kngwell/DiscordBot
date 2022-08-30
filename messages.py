import discord
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, client):
      self.client = client

    @commands.command()
    async def ahhh(self, ctx):
      message = ctx.message
      await message.channel.send('AAAAAHHHHHHHHHHHHH')

    @commands.command()
    async def holdon(self, ctx):
      message = ctx.message
      await message.channel.send("Hold on hold on hold on. Her sister was a witch right? And what was her sister? A princess, the wicked witch of the east bro. You're gonna look at me and you're gonna tell me that I'm wrong? Am I wrong? She wore a crown and she came down in a bubble, Doug. Grow up bro, grow up.")
      
    @commands.command()
    async def moonmen(self, ctx):
      message = ctx.message
      await message.channel.send("if there were two guys on the moon, and one killed the other with a rock, how messed up would that be?")
      
async def setup(client):
 await client.add_cog(Messages(client))