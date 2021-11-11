import datetime
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	
    async def is_owner(ctx):
        return ctx.author.id == 143423810014674945
    
    #Admin help
    @commands.command(name='ahelp',help='Admin help')
    @commands.check(is_owner)
    async def ahelp(self, ctx):
        print("Admin help sent!")
        embed = discord.Embed(title="Admin Help", description="It's like normal help, but for admins.", color=0x771c85)
        embed.set_author(name='Spookbot',
        icon_url="https://i.imgur.com/O5UsZ8G.png")
        embed.add_field(name="<:glaceon:657315337879945256>Commands:", value='''`ahelp`: Help, but for admin commands.
`amiadmin`: It's like a vibe check, but so much worse.
`dmuser [user id] [message]`: Send a DM to a specified user.
`msgsend [channel id] [message]`: Send a message to a specified channel.''', inline=False)
        await ctx.channel.send(embed=embed)
    @ahelp.error
    async def ahelp_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
            
    #Am I admin?
    @commands.command(name='amiadmin', help='It\'s like a vibe check, but worse.')
    @commands.check(is_owner)
    async def amiadmin(self, ctx):
        print("An admin was checked: {}".format(ctx.author.name))
        await ctx.channel.send("You are an admin!")
    @amiadmin.error
    async def amiadmin_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')

    #Send message to specified channel
    @commands.command(name='msgsend', help="Sends a message as bot to a specified channel.")
    @commands.check(is_owner)
    async def msgsend(self, ctx, cnl, msg):
        print("Message sent to another channel: {}".format(msg))
        channel = self.bot.get_channel(int(cnl))
        await channel.send(msg)
    @msgsend.error
    async def msgsend_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
        else:
            raise error
            
    #DM User
    @commands.command(name='dmuser', help="Sends a DM to a specified user.")
    @commands.check(is_owner)
    async def dmuser(self, ctx, usr, msg):
        print("DM sent to {}:".format(usr) + " {}".format(msg))
        user = self.bot.get_user(int(usr))
        await user.send("{}".format(msg))
    @msgsend.error
    async def msgsend_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
        else:
            raise error

def setup(bot):
    bot.add_cog(Admin(bot))