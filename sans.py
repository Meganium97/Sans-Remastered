print('Loading...')
import subprocess
from inspect import cleandoc
from typing import Union
import os
import discord
from discord.ext import commands

def make_embed(title=None, description=None, author=None, thumbnail=None, url=None, color=None, image=None, name=None) -> discord.Embed: 
    """Cleaner way to make embeds
    Thumbnail and author are taken as kwargs, title is default "Guide" """ 
    if isinstance(color, int):
        color = discord.Color(color)
    
    embed = discord.Embed(
        title=title,
        color=color,
        url=url,
        description=description
    )
    if name is not None:   embed.set_author(name=name)
    if image is not None:   embed.set_image(url=image)
    if thumbnail is not None:   embed.set_thumbnail(url=thumbnail)
    return embed

bot = commands.Bot(command_prefix=("."), case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))
bot.help_command = commands.DefaultHelpCommand(dm_help=None)


home_path = os.path.dirname(os.path.realpath(__file__)) # previously token_dir
with open(home_path + "/token.json") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')
    print(f'We have logged in as {bot.user}')
