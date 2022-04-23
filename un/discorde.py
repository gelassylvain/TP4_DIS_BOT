import discord
from discord.ext import commands

class Discorde(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} est prêt !')


##GELAS SYLVAIN 32
