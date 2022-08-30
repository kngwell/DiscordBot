import discord
from discord.ext import commands


class Reactions(commands.Cog):
    def __init__(self, client):
      self.client = client 
      self.role_message_id = 1013340925591818311  
      self.emoji_to_role = {
            discord.PartialEmoji(name='🖥️'): 1013301538774597682,
            discord.PartialEmoji(name='🟡'): 1013301344368607262,  
        }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives role when message reacted to."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.client.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:        
            return

        try:
          
            await payload.member.add_roles(role)
        except discord.HTTPException: return
    @commands.Cog.listener()   
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
      """Removes role if reaction is removed."""

      if payload.message_id != self.role_message_id:
          return

      guild = self.client.get_guild(payload.guild_id)
      if guild is None:

          return

      try:
          role_id = self.emoji_to_role[payload.emoji]
      except KeyError:

          return

      role = guild.get_role(role_id)
      if role is None:
     
          return


      member = guild.get_member(payload.user_id)
      if member is None:
  
          return

      try:
 
          await member.remove_roles(role)
      except discord.HTTPException: return

async def setup(client):
 await client.add_cog(Reactions(client))