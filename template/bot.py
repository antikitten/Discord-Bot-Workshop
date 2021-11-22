import random
import discord
import os
import images

from discord.ext import commands
from dotenv import load_dotenv

# Load in the Discord API key from your .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialise a bot object with a command prefix
bot = commands.Bot(command_prefix='!!')


@bot.event
async def on_ready():
    print('Bot running')


@bot.event
async def on_message(message):
    if message.content.lower() == 'hello':
        await message.channel.send(f'hello {message.author.mention}')
    await bot.process_commands(message)


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name='rps')
async def rps(ctx, playerchoice):
    ...


@bot.command(name='santa')
async def santa(ctx):
    ...


@bot.command(name='moustache')
async def moustache(ctx):
    ...

# Start the bot using the API key
bot.run(TOKEN)
