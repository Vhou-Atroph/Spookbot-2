import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime

#Bot info
prefix='s!'
desc='A new version of Spookbot by Vhou.'
version='v1.4'

#Setup
bot = Bot(command_prefix=prefix, description=desc)
bot.remove_command('help')
token='token'

#Startup events
@bot.event
async def on_ready():
    print('------')
    print('Spook time!')
    print('Logged in as...')
    print('USER: {}'.format(bot.user.name))
    print('ID: {}'.format(bot.user.id))
    print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    print('------')
    await bot.change_presence(activity=discord.Game(name='around'))

#Cogs
initial_extensions=['cogs.admin',
'cogs.core',
'cogs.fun',
'cogs.monhun',
'cogs.toontown']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#Run bot
bot.run(token)