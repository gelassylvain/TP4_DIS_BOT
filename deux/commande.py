import discord


class Commande(discord.ext.commands.Cog, name='Commandes'):
    def __init__(self, bot):
        self.bot = bot

    ##### LE BOT ENVOIT UN MESSAGE DE BIENVENU AU NOUVEL UTILISATEUR  #####
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} est parmi nous et on lui dit bienvenue :) !')

    ##### BOT REPOND 'BONJOUR' #####
    @discord.ext.commands.command(name="Bonjour")
    async def addhoc_play(self, ctx):
        await ctx.send(f'Bonjour {ctx.author.name}')

    ##### LE BOT RENVOI LE MESSAGE ET SPECIFIE L'UTILISATEUR EN LE NOMANT  #####
    @discord.ext.commands.command(name="Sylvain")
    async def addhoc_pla(self, ctx):
        await ctx.send(f'Sylvain est le mot écrit par {ctx.author.name}')

    ##### SUPRESSION DE MESSAGES  #####
    @discord.ext.commands.command(name="sup")
    async def on_message(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            
            for each_message in messages:
                await each_message.delete() 
        
##GELAS SYLVAIN 32


