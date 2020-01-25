import os
import random
import discord as ds
from discord.ext import commands
from dotenv import load_dotenv

#environment variables
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = ds.Client()
bot = commands.Bot(command_prefix='!')

#On bot establishing connection
@client.event
async def on_ready():
    guild = ds.utils.get(client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#on member joining
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command()
async def color(ctx):
    colors = ["red", "green", "blue"]
    ctx.send(random.choice(colors))

@bot.command(name='8ball')
async def eightBall(ctx, args):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    ctx.send(random.choice(possible_responses))

client.run(token)