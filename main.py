import discord
import json


from discord.ext import commands

import config
from config import spotify_info

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Я запущен!")
    with open('data.txt', 'w') as outfile:
        json.dump(config.user)



@bot.command()
async def hi(ctx):
    await ctx.send('Hi')
    print(f"user {str(ctx.message.author.name)} use command {hi} ")


@bot.command(name="inf")
async def _music(ctx):
    await ctx.send(f'your name : {spotify_info["USERNAME"]}')
    await ctx.send(json.dumps(config.user, sort_keys=True, indent=4))


@bot.command(name='ui')
async def _user_image(ctx):
    await ctx.send(json.dumps(config.user))


bot.run('')
