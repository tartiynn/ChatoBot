# ChatoBot

## Comment contribuer ?
### Devenir collaborateurice du projet

Même si ce projet est public, il faut être contributeur pour pouvoir pousser de nouvelles fonctionnalités. Envoie-moi un DM sur Discord (mon pseudo : Nafyn) avec ton nom d'utilisateurice Github ou ton adresse mail pour que je puisse t'ajouter à l'équipe.

### Cloner la source

Installe git si tu ne l'as pas encore. Pour Windows : https://gitforwindows.org/

Dans ton terminal, utilise :
```
git clone https://github.com/tartiynn/ChatoBot.git
```
Cela va mettre les fichiers sources dans un dossier ChatoBot, et tu pourras les modifier.

### Créer une commande

Pour l'instant, il n'y a qu'un seul fichier python, ```bot.py```. Il contient l'initialisation du bot et l'intégralité de ses commandes, ainsi que son lancement. On peut envisager de séparer ce fichier en plusieurs fichiers si le bot devient conséquent.

La norme ```snake_case``` (mots séparés par le caractère ```_``` et tout en minuscules) est utilisée pour le nommage des variables et fonctions.

Voici un exemple de commande :
```Python
# !poll [Proposition]
# ---
# Le bot ajoutera les emojis 👍 (oui), 👎 (non) et 🤷 (je ne sais pas / sans avis) pour ne pas avoir a les rechercher.
# Permet de demander un avis sur des proposition binaires.
@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')
    await ctx.message.add_reaction('🤷')
```

Elle est composée de :
- **Une description :** Elle contient l'usage, c'est à dire la façon dont la commande doit être appelée, et une description de l'effet de la commande.
- **Un décorateur :** L'objet ```bot``` est défini au début du fichier, avec comme préfixe "!". ```@bot.command()``` signifie que la fonction qui suit doit être appelée par le bot lorsqu'on tape un message qui commence par ```![nom_de_la_fonction]```, ici ```!poll```.
- **Une fonction** qui a :
  - *Un mot-clé async*, ce qui signifie que la fonction est asynchrone : elle va attendre la fin de chaque action qu'on demande au bot de faire avant de continuer.
  - *Des arguments*, ici ```ctx```. ```ctx``` est le contexte du message qui a appelé la commande : il contient toutes les informations fournies par l'API Discord sur le message : son contenu, son expéditeurice, le channel dans lequel il a été envoyé, ses réactions, l'heure d'envoi etc. Il permet par exemple dans la fonction de lui rajouter des réactions. On peut aussi prendre d'autres arguments après le contexte : ```arg1, arg2, ...``` permet de découper le reste du message en mots que l'o peut réutiliser dans la fonction. Autre utilisation : une fonction ```async def fn(ctx, *, args)``` permet de retrouver tout le message moins la commande dans args.
  - *Un corps*, qui permet de traiter les arguments et de faire agir le bot. On utilise [```Discord.py```](https://discordpy.readthedocs.io/en/stable/api.html) qui a de nombreuses fonctionnalités

Chaque commande est également référencée dans la commande help, qui est faite à la main pour pouvoir être plus maniable.

### Tester le bot

Pour l'instant, le bot n'est pas déployé, je recommande donc de tester en local avant de pousser quoi que ce soit. Un tutoriel pour créer son bot se trouve [ici](https://realpython.com/how-to-make-a-discord-bot-python/). La partie qui nous intéresse est celle sur le *developer portal*. Il explique également comment lancer le bot localement.

Avant de tester localement, il faut créer un fichier ```.env``` dans le dossier racine, et y mettre les deux variables ```DISCORD_TOKEN``` et ```GUILD_TOKEN```, pour pouvoir lancer le bot. Cette partie est également expliquée dans le tutoriel.

### Pousser les modifications

- *Merci de ne pas pousser de modifications qui n'ont pas été testées. Même si Python est robuste, ça serait bête que notre ChatoBot ne tienne plus le coup pour un oubli.*
- *Merci de documenter ce qui est fait, pour que les autres contributeurices puissent comprendre le code à tout moment, et dans un souci de partage des connaissances.*
- *On part sur un principe de confiance. Cependant, je me réserve le droit d'enlever un commit s'il peut porter préjudice aux membres du Chateau, porter atteinte à leur vie privée, ou si une commande malveillante est ajoutée.*

Il n'y a pas de système de pull request pour le moment (du moins je ne l'ai pas configuré), il suffit donc de commit et push les modifications. Le fichier ```.env``` est ignoré dans le but de ne pas pousser d'informations sensibles, ce qui nous intéresse est seulement le fichier ```bot.py``` (et ce README, s'il est modifié).

## Commandes supportées
### !help
Usage : 
```
!help [Commande]
```

### !pardon
Usage : 
```
!pardon
```

### !poll
Usage : 
```
!poll [Proposition / Question]
```

### !multipoll
Usage : 
```
!multipoll [Question]
[Emoji 1] [Option 1]
[Emoji 2] [Option 2]
...
[Emoji n] [Option n]
```

### !threads
Usage : 
```
!threads
```
