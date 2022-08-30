import os
import discord


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 1013340925591818311  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 1013301538774597682,
            discord.PartialEmoji(name='🟡'): 0,  # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name='green', id=0): 0,  # ID of the role associated with a partial emoji's ID.
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
        
            return

        try:
          
            await payload.member.add_roles(role)
        except discord.HTTPException:
			
			pass
            

async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""

        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
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
        except discord.HTTPException:
 
            pass


intents = discord.Intents.default()
intents.members = True
my_secret = os.environ['TOKEN']
client = MyClient(intents=intents)
client.run(my_secret)