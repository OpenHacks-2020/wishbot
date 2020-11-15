import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from scraper import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WISHLIST = {}
DIRECT_WISHLIST = {}

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
            if 'link' in message_content:
                gifts = "\n".join(DIRECT_WISHLIST[name])
            else:
                gifts = "\n".join(WISHLIST[name])
            await message.channel.send('__**Current gifts for {0}:\n{1}**__'.format(name.capitalize(), gifts))
        else:
            await message.channel.send('***There are no gifts selected for {0}.***'.format(name.capitalize()))
    elif message_content.startswith('remove'):
        contents = message_content.split()[1:]
        contents[0] = contents[0].split("'")[0]
        response = remove_from(contents)
        await message.channel.send('__**' + response + '**__')
    elif message_content.startswith('suggest'):
        recipient = message_content.split()[2]
        price_range = message_content.split()[4]
        response = suggestion(recipient,price_range)
        await message.channel.send('__**' + response + '**__')
    elif message_content.startswith('advice'):
        recipient = message_content.split()[2:]
        response = advisor(recipient)
        await message.channel.send('__**' + response + '**__')
    elif message_content == 'help':
        response = help_command()
        await message.channel.send(response)        

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

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
            webpage = 'https://www.etsy.com/search?q={0}'.format(desired_gift)
            webpage_direct = scrape_link(webpage)
            if recipient in WISHLIST:
                WISHLIST[recipient].append(webpage)
                DIRECT_WISHLIST[recipient].append(webpage_direct)
            else:
                WISHLIST[recipient] = [webpage]
                DIRECT_WISHLIST[recipient] = [webpage_direct]
            return ' '.join(contents[1:]).capitalize() + " added to {0}'s wishlist".format(recipient.capitalize())
    else:
        return 'You typed nothing'

def remove_from(contents):
    '''Removes Etsy URL from WISHLIST entry associated with the RECIPIENT and returns a string confirming gift removal.'''
    if len(contents) >= 2:
        recipient = contents[0]
        desired_gift = '+'.join(contents[1:])
        webpage = 'https://www.etsy.com/search?q={0}'.format(desired_gift)
        if recipient in WISHLIST:
            webpage_direct = scrape_link(webpage)
            WISHLIST[recipient].remove(webpage)
            DIRECT_WISHLIST[recipient].remove(webpage_direct)
        else:
            return 'Unknown recipient.'
        return ' '.join(contents[1:]).capitalize() + " removed from {0}'s wishlist".format(recipient.capitalize())
    else:
        return 'You typed nothing'
    
def suggestion(recipient, price_range):
    '''Suggests a present based on the inputted price range'''
    if price_range == '20':
        gift = random.choice(open('giftunder20.txt').readlines())
    elif price_range == '50':
        gift = random.choice(open('giftunder50.txt').readlines())
    elif price_range == '100':
        gift = random.choice(open('giftunder100.txt').readlines())
    else:
        return "Nobody deserves a present that costs that much. Go donate to charity."
    return give_command([recipient,gift])

def advisor(contents):
    '''Gives you advice about whether you should give the person in question a present or not'''
    possibilities = [1,0]
    advice = random.choice(possibilities)
    if advice:
        return 'You should give {0} a present.'.format(contents[0])
    else:
        return 'Forget {0}. Buy yourself something nice.'.format(contents[0])

def help_command():

# @bot.command(name='CA', help='Gives the number of current COVID-19 cases in California')
# async def number_cases(ctx):
#     cases = 'CA CASES PLACEHOLDER'
#     response = cases
#     await ctx.send(response)

client.run(TOKEN)
#bot.run(TOKEN)
