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

# If you want to be recognised, put your name in

@bot.group()
async def contributors(ctx):
    '''Links contributors to the code'''
    if ctx.invoked_subcommand is None:
        await ctx.send('Which one? Current or old?')
        
@contributors.command()
async def current(ctx):
    '''Lists currect Sans contributors'''
    embed = discord.Embed(
        title="List of current Sans contributors",
        description=cleandoc("""
            Meganium97 (Dire) - Current leading coder
            Lazr - Removed some useless shit
        """)
    )
    
    await ctx.send(embed=embed)

@contributors.command()
async def old(ctx):
    '''Lists the old Sans contributors'''
    embed = discord.Embed(
        title="List of old Sans contributors",
        description=cleandoc("""
            Lazr1026 - Creator and programmer
            476MHz (Radeon) - Programmer
            Uwuham - Not very much, he makes commits sometimes
            Techmuse - PR'd useful shit
            Gnome! - Cleaned everything up massively
            ItsPizzaTime1501 - Helped with proper licensing
            bleck9999 - Fixed Gnomes mistakes
            Maretu (ray) - Fixed our terrible grammar
            Meganium97 (Dire) - Idk, what are you asking me for?
            Glazed_Belmont - Fixed the paths not being universal
        """)
    )
    
    await ctx.send(embed=embed)

# now onto the actual commands

@bot.command()
async def test(ctx):
    '''sends test, what did you expect?'''
    await ctx.send('test')
    
@bot.command()
async def snas(ctx):
    '''fortnite battle royale'''
    await ctx.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

@bot.command()
async def sans(ctx):
    '''Links the github repo for Sans'''
    embed = make_embed(
        title="Sans",
        author="Maintained by Meganium97",
        color=discord.Color.green(),
        thumbnail="https://i.imgur.com/AkOLH6q.png",
        url="https://github.com/Meganium97/Sans-Remastered",
        description="Sans, The discord bot that is kinda useful!"
    )

    await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin', 'Sans Contributor')
async def update(ctx):
    await ctx.send("Updating code. The bot will be down for a few seconds, if this doesnt break the code.")
    subprocess.run(['bash', home_path + '/update.sh'])

@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin')
async def ban(ctx, member: discord.User = None, reason="[no reason specified]"):
    '''does what it says on the tin'''
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself.")
        return
    reasonraw = ctx.message.content[28:]
    message = f"You have been banned from {ctx.guild.name} for the reason {reasonraw}"
    await ctx.guild.ban(member, reason=reasonraw, delete_message_days=0)
    await ctx.channel.send(f"{member} has been b&. 👍")
    await member.send(message)
    
@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin', 'Helper')
async def kick(ctx, member: discord.Member, *, reason=0):
    '''does what it says on the tin'''
    await member.kick(reason=reason, delete_message_days=0)
    send = f"user {member.name} has been kicked."
    await ctx.send(send)

@bot.command()
@commands.has_any_role('Owner', 'Staff', 'Admin', 'Helper', 'Sans Contributor')
async def say(ctx, message):
    '''does what it says on the tin (Sans Contributors+)'''
    await ctx.message.delete()
    await ctx.send(ctx.message.content[5:])
    
@bot.command(aliases=["pfp"])
async def profile(ctx, user: discord.User):
    '''Fetch a user's profile icon'''
    await ctx.send(f"Profile image for user: {user.name}")
    pfp = user.avatar_url
    await ctx.send(pfp)
    
@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! Latency is {int(bot.latency * 1000)} ms!')

@bot.command()
@commands.bot_has_permissions(read_messages=True, send_messages=True)
async def suggest(self, ctx, *, suggestion):
    "Suggests a new feature!"

    if suggestion.lower().replace("*", "") == "suggestion":
        return await ctx.send("Hey! You are meant to replace `*suggestion*` with your actual suggestion!")

    if not await self.bot.blocked_users.check(ctx.message.author):
        webhook = await ensure_webhook(self.bot.channels["suggestions"], "SUGGESTIONS")
        files = [await attachment.to_file() for attachment in ctx.message.attachments]

        await webhook.send(suggestion, username=str(ctx.author), avatar_url=ctx.author.avatar_url, files=files)

    await ctx.send("Suggestion noted")

# General fun stuff

@bot.command()
async def bean(ctx, u: discord.Member):
    '''BEAN!!!'''
    await ctx.send(f"{u.mention} Get Beaned!!!")
bot.run(token)
