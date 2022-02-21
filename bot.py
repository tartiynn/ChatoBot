import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import emoji

load_dotenv()

# Les tokens sont stockes à la racine du projet, dans un fichier .env
# On les recupere ici pour pouvoir les utiliser
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_TOKEN = os.getenv('GUILD_TOKEN')

# On cree un bot, 
# command_prefix="!" -> on definit son prefixe : les commandes doivent commencer par le caractere "!", 
# help_command=None -> on enleve la commande help par defaut
bot = commands.Bot(command_prefix="!", help_command=None)
bot.pardons = 0 # On initialise les variables du bot

# !help [Commande]
# ---
# Donne des precisions sur l'usage de la commande.
# Si aucune commande n'est renseignee, donne une liste des commandes avec leurs usages.
@bot.command()
async def help(ctx, *, args=""):
    commands = {
      "help" : "**Help**\n\
        Usage : *!help [Commande]*\n\
        Donne des précisions sur l'usage de la commande.\n\
        Si aucune commande n'est donnée, donne une liste des commande avec leurs usages.",
      "pardon" : "**Pardon**\n\
        Usage : *!pardon*\n\
        Incrémente le compteur de pardons, et affiche l'état actuel de la \"cagnotte\".",
      "poll" : "**Poll**\n\
        Usage : *!poll [Proposition]*\n\
        Le bot ajoutera les emojis 👍 (oui), 👎 (non) et 🤷 (je ne sais pas / sans avis) pour ne pas avoir à les rechercher.\n\
        Permet de demander un avis sur des proposition binaires.",
      "multipoll": "**Multipoll**\n\
        Usage : *!multipoll [Question]\n\
        [Emoji] [Proposition 1]\n\
        [Emoji] [Proposition 2]\n\
        [...]*\n\
        Le bot ajoutera les emojis qui se trouvent en début de ligne.\n\
        Le multipoll permet des polls plus complets, avec des emojis définis par l'utilisateur.\n\
        /!\ Ne mettre que des emojis differents.",
      "threads" : "**Threads**\n\
        *Incomplet*\n\
        Usage: *!threads*\n\
        Donne une liste des threads référencés. A améliorer lorsque la lib python intégrera les threads."
    }

    message = ""
    if (args == "" or args == None):
        message = "\n\n".join(list(commands.values()))
    else:
        cmd = args.split(" ")[0]
        if (cmd in ["help", "!help"]):
            message = commands["help"]
        if (cmd in ["pardon", "!pardon"]):
            message = commands["pardon"]
        if (cmd in ["poll", "!poll"]):
            message = commands["poll"]
        if (cmd in ["multipoll", "!multipoll"]):
            message = commands["multipoll"]
        if (cmd in ["threads", "!threads"]):
            message = commands["threads"]
    await ctx.send(message)

# !pardon
# ---
# Incremente le compteur de pardons, et affiche l'etat actuel de la "cagnotte".
@bot.command()
async def pardon(ctx):
    bot.pardons += 1

    # On va choisir une phrase au hasard dans ce tableau
    phrases = [
      "Et un euro de plus pour le chateau !", 
      "Des clochettes, des clochettes !", 
      "Bientôt la colloc !",
      "Plus que " + str(1000000 - bot.pardons) + " clochettes avant le chateau !",
      "Merci pour votre participation à l'effort général !",
      "Oups !",
      "On avait dit pas de pardon !"
      ]

    message = random.choice(phrases) + " Nous en sommes à " + str(bot.pardons) + " euro" + ("s" if bot.pardons != 1 else "") + "."
    await ctx.send(message)

# !poll [Proposition]
# ---
# Le bot ajoutera les emojis 👍 (oui), 👎 (non) et 🤷 (je ne sais pas / sans avis) pour ne pas avoir a les rechercher.
# Permet de demander un avis sur des proposition binaires.
@bot.command()
async def poll(ctx, arg):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')
    await ctx.message.add_reaction('🤷')

# !multipoll [Question]
# [Emoji] [Proposition 1]
# [Emoji] [Proposition 2]
# ...
# ---
# Le bot ajoutera les emojis de debut de ligne. 
# Le multipoll permet des polls plus complets, avec des emojis definis par l'utilisateur.
# /!\ Ne mettre que des emojis differents.
@bot.command()
async def multipoll(ctx, *, arg):
    answers = [line.split(" ")[0] for line in arg.split("\n") if line[0] in emoji.UNICODE_EMOJI['en']]
    for answer in answers : 
      await ctx.message.add_reaction(answer)

# !threads
# ---
# Donne une liste des threads references. A ameliorer lorsque la lib python evoluera.
@bot.command()
async def threads(ctx):
    message = "**Liste des threads du Discord :**\n\
      *Poésie > Cadavre exquis* : prendre part à la création de phrases collaboratives."
    await ctx.send(message)

bot.run(TOKEN)
