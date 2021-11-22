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
    playerchoice = playerchoice.lower()
    choices = ['rock', 'paper', 'scissors']
    botchoice = random.choice(choices)

    if playerchoice.lower() not in choices:
        await ctx.send('Please enter a valid input')

    await ctx.send(f'I choose {botchoice}!')

    if playerchoice == botchoice:
        await ctx.send("Tie!")
    elif playerchoice == "rock":
        if botchoice == "paper":
            await ctx.send("You lose!")
        else:
            await ctx.send("You win!")
    elif playerchoice == "paper":
        if botchoice == "scissors":
            await ctx.send("You lose!")
        else:
            await ctx.send("You win!")
    elif playerchoice == "scissors":
        if botchoice == "rock":
            await ctx.send("You lose!")
        else:
            await ctx.send("You win!")

@bot.command(name='santa')
async def santa(ctx):
    filepath = 'avi.png'
    await ctx.author.avatar_url_as(format='png', size=4096).save(filepath)
    new_avi = images.add_santa_hat(filepath)
    new_avi.save('santa.png')
    await ctx.send(file=discord.File('santa.png'))

@bot.command(name='moustache')
async def moustache(ctx):
    filepath = 'avi.png'
    await ctx.author.avatar_url_as(format='png', size=4096).save(filepath)
    new_avi = images.add_santa_hat(filepath)
    new_avi.save('moustache.png')
    await ctx.send(file=discord.File('moustache.png'))


# Start the bot using the API key
bot.run(TOKEN)
