print('Loading...')
import subprocess
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=("."), case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))

home_path = os.path.dirname(os.path.realpath(__file__)) # previously token_dir
with open(home_path + "/token.json") as tokenfile:
    token = tokenfile.read()

@bot.event
async def on_ready():
    print('Ready.')
    print(f'We have logged in as {bot.user}')
    bot.channel = bot.get_channel(770100020736688128)

# userphone shit. Hardcoded. You can change that.

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id in (794603732947042337, ):
        
        webhooks = await bot.channel.webhooks()
        if len(webhooks) == 0:
            webhook = await bot.channel.create_webhook(name="Receiving Webhook")
        else:
            webhook = webhooks[0]
        await webhook.send(message.content, embeds=message.embeds, username=message.author.display_name, avatar_url=str(message.author.avatar_url))     
bot.run(token)
