import discord
from un.discorde import Discorde
from deux.commande import Commande


def main():
    token = "" ##JE N'AI PAS MIS MON TOKEN CAR EN FAISANT UN COMMIT/PUSH, DISCORD M'ENVOIT UN MESSAGE DE PREVENTION ET SUPPRIME MON BOT


    intents = discord.Intents.default()
    intents.members = True

    bot = Discorde(
        command_prefix='$', 
        intents=intents
    )

    bot.add_cog(Commande(bot))

    bot.run(token)


if __name__ == '__main__':
    main()

##GELAS SYLVAIN 32