import json
import discord
import config
from discord.ext import commands
from config import spotify_info
from connectdb import cursor

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Я запущен!")
    print(cursor.fetchall())


@bot.command(name='hi')
async def hi(ctx):
    await ctx.send(f"user {str(ctx.message.author.name)} use command {hi} ")
    print(f"user {str(ctx.message.author.name)} use command {hi} ")


@bot.command(name="inf")
async def _music(ctx):
    await ctx.send(f'your name : {spotify_info["USERNAME"]}')
    await ctx.send(json.dumps(config.user, sort_keys=True, indent=4))


@bot.command(name='ui')
async def _user_image(ctx):
    await ctx.send()


bot.run(config.settings["token"])
