import discord
import config
from discord.ext import commands
from discord.utils import get

client = commands.Bot(description = "Adds reactions automatically to suggestions", command_prefix = "!")

@client.event
async def on_ready():
    global channel
    print("#################\n# Bot is online #\n#################")
    print("Running as: " + client.user.name)
    print("ID: " + client.user.id)
    print("Discord.py: " + discord.__version__)
    print("Created by Accieo#8858")
    channel = client.get_channel(config.channelID)

@client.event
async def on_message(ctx):
    if ctx.channel == channel:
        for emoji in config.reactionEmojis:
            await client.add_reaction(ctx, emoji)

client.run(config.token)
