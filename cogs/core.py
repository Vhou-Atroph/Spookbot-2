import datetime
import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Help
    @commands.command(name='help',help='help')
    async def help(self, ctx, category='help'):
        print('Sent help command as requested by: {}'.format(ctx.author.name))
        helps=['help','bot','fun','monhun','toontown']
        
        #Basic help
        if category=='help':
            embed = discord.Embed(title="Help", description="Type `s!help <category>` for specific commands in each category!", color=0x771c85)
            embed.add_field(name="Help categories:", value=''':robot:`bot`: Core bot commands!
:game_die:`fun`: Fun commands!
<:rathalos:657007621055840283>`monhun`: Monster Hunter commands!
<:tewtow:657007812471291918>`toontown`: Toontown commands!''', inline=False)
            await ctx.channel.send(embed=embed)
            
        #Core help
        if category=='bot':
            embed = discord.Embed(title=":robot:Bot help", description="Core bot commands!", color=0x771c85)
            embed.add_field(name="Commands:", value='''`help`: Command info
`info`: About Spookbot.
`invite`: Invite Spookbot to another server
`ping`: Pong''', inline=False)
            await ctx.channel.send(embed=embed)
            
        #Fun help
        if category=='fun':
            embed = discord.Embed(title=":game_die:Fun help", description="Fun commands!", color=0x771c85)
            embed.add_field(name="Commands:", value='''`droll <#>`: Roll a die of specified size [Default 6]
''', inline=False)
            await ctx.channel.send(embed=embed)
        
        #Monster Hunter help
        if category=='monhun':
            embed = discord.Embed(title="<:rathalos:657007621055840283>Monster Hunter help", description="Monster Hunter commands!", color=0x771c85)
            embed.add_field(name="Commands:", value='''`mhr hunt`: Chooses a random monster from Monster Hunter Rise.
            `mhr locale`: Chooses a random locale from Monster Hunter Rise.
`mhr party`: Chooses a random party composition for your next quest.
`mhweapon`: Chooses a random weapon for your next quest.
`mhw hunt`: Chooses a random monster from Monster Hunter World.
`mhw locale`: Chooses a random locale from Monster Hunter World.
''', inline=False)
            await ctx.channel.send(embed=embed)
            
        #Toontown help
        if category=='toontown':
            embed = discord.Embed(title="<:tewtow:657007812471291918>Toontown help", description="Toontown commands!", color=0x771c85)
            embed.add_field(name="Commands:", value='''`coghp <lvl>`: Evaluates cog health for levels 1-12.
`makeatoon`: Generates a random toon.
`namett`: Generates a random toon name.
`sillymeter`: Silly Meter stats.''', inline=False)
            await ctx.channel.send(embed=embed)
            
        #Handling other responses.
        if category not in helps:
            await ctx.channel.send("This category of help does not exist.")
    
    #Ping
    @commands.command(name='ping',help='pong')
    async def ping(self, ctx):
        print('Ping at {}.'.format(datetime.datetime.now()))
        await ctx.channel.send('Pong')
        
    #Invite
    @commands.command(name='invite', help="Invite the bot to your server")
    async def invite(self, ctx):
        print("Invite requested.")
        embed = discord.Embed(title="Invite SpookBot!", description="Invite me to your server!", color=0x771c85)
        embed.set_thumbnail(url="https://i.imgur.com/MTmbIpO.jpg")
        embed.add_field(name="Link:", value="[Click here!](https://discordapp.com/api/oauth2/authorize?client_id=650883667203194880&permissions=392256&scope=bot)", inline=False)
        await ctx.channel.send(embed=embed)
        
    #Info
    @commands.command(name='info',help='Bot info')
    async def info(self, ctx):
        print("Bot info sent!")
        embed=discord.Embed(title="About SpookBot:",description="Spook time!", color=0x771c85)
        embed.set_author(name='Spookbot',
        icon_url="https://i.imgur.com/pH241lv.png")
        embed.set_thumbnail(url='https://i.imgur.com/JuqlXQa.jpg')
        embed.add_field(name="Version:",value='1.4',inline=False)
        embed.add_field(name="User ID:",value=self.bot.user.id,inline=False)
        embed.add_field(name="Number of servers:", value=str(len(self.bot.guilds)), inline=False)
        await ctx.channel.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Core(bot))