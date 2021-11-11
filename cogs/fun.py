import random
from random import *
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Dice roll
    @commands.command(name='droll',help='Rolls a die.')
    async def droll(self, ctx, n='6'):
        n = int(n)
        die = randint(1, n)
        print("Rolled a {}".format(die))
        await ctx.channel.send('You rolled a {}!'.format(die))
    
def setup(bot):
    bot.add_cog(Fun(bot))