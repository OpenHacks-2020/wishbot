import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WISHLIST = {}

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the CovidUpdates discord server - created for the OpenHacks 2020 Hackathon!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content.lower().strip()
    if message_content.startswith('give'):
        #Calls give_command on the rest of the message, which includes
        #the name of the desired gift recipient.
        response = give_command(message_content.split()[1:])
        await message.channel.send('__**' + response + '**__')
    elif message_content.startswith('retrieve'):
        name = message_content.split()[1]
        name = name.split("'")[0]
        if name in WISHLIST:
            gifts = "\n".join(WISHLIST[name])
            await message.channel.send('__**Current gifts for {0}:\n{1}**__'.format(name.capitalize(), gifts))
        else:
            await message.channel.send('***There are no gifts selected for {0}.***'.format(name.capitalize()))
            

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

#CUSTOM COMMANDS

#GIVE
def give_command(contents):
    '''Adds Etsy URL to WISHLIST entry associated with the RECIPIENT and returns a string confirming gift addition.'''
    if len(contents) >= 2:
        recipient = contents[0]
        if contents[1] == 'a' or contents[1] == 'an':
            contents.pop(1)
            return give_command(contents)
        else:
            desired_gift = '+'.join(contents[1:])
            if recipient in WISHLIST:
                WISHLIST[recipient].append('https://www.etsy.com/search?q={0}'.format(desired_gift))
            else:
                WISHLIST[recipient] = ['https://www.etsy.com/search?q={0}'.format(desired_gift)]
            return ' '.join(contents[1:]).capitalize() + " added to {0}'s wishlist".format(recipient.capitalize())
    else:
        return 'You typed nothing'

# @bot.command(name='CA', help='Gives the number of current COVID-19 cases in California')
# async def number_cases(ctx):
#     cases = 'CA CASES PLACEHOLDER'
#     response = cases
#     await ctx.send(response)

client.run(TOKEN)
#bot.run(TOKEN)