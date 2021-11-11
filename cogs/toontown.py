import random
from random import *
import requests
import discord
from discord.ext import commands

class Toontown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	
    #Cog health calculator
    @commands.command(name='coghp',help='Evaluates cog health at levels 1-12')
    async def coghp(self, ctx, lvl):
        lvl = int(lvl)
        if lvl > 0 and lvl < 12:
            hp = (lvl+1)*(lvl+2)
            print('Cog health evaluated! Cog health:{}'.format(hp))
            await ctx.channel.send('The cog has {} health.'.format(hp))
        if lvl > 11 and lvl < 13:
            print('Cog health evaluated! Cog health: 200')
            await ctx.channel.send('The cog has 200 health.')
        if lvl < 1:
            await ctx.channel.send('Please send a different number.')
        if lvl > 12:
            await ctx.channel.send('Please send a different number.')

    #Make a Toon name
    @commands.command(name='namett', help='Chooses a random cog boss from Toontown.')
    async def namett(self, ctx):
            g = ['m', 'f']
            gender = choice(g)
            if gender == 'm':
                title = ['Baron','Big','Cap\'n','Captain','Chef','Chief','Coach','Colonel','Cool','Count','Crazy','Daring','Deputy','Dippy','Doctor','Dr.','Duke','Fat','Good ol\'','Grand ol\'',
                'Grumpy','Judge','King','Little','Loopy','Loud','Lucky','Master','Mister','Mr.','Noisy','Prince','Prof.','Sergeant','Sheriff','Silly','Sir','Skinny','Super','Ugly','Weird'] 
                #God I hope TTR doesn't add anymore names, I haven't even done the rest yet and this is horrible
                first = ["Albert","Alvin","Arnold","Astro","B.D.","Banjo","Barney","Bart","Batty","Beany","Bebop","Bentley","Beppo","Bert","Billy","Bingo","Binky","Biscuit","Bizzy","Blinky","Bob",
                "Bonbon","Bongo","Bonkers","Bonzo","Boo Boo","Boots","Bouncey","Bruce","Bud","Buford","Bumpy","Bunky","Buster","Butch","Buzz","C.J.","C.W.","Casper","Cecil","Chester","Chewy","Chip",
                "Chipper","Chirpy","Chunky","Clancy","Clarence","Cliff","Clyde","Coconut","Comet","Cookie","Corky","Corny","Cranky","Crazy","Cricket","Crumbly","Cuckoo","Curly","Curt","Daffy","Dave",
                "Davey","David","Dinky","Dizzy","Domino","Dot","Drippy","Droopy","Dudley","Duke","Dusty","Dynamite","Elmer","Ernie","Fancy","Fangs","Felix","Finn","Fireball","Flapjack","Flappy",
                "Fleabag","Flint","Flip","Fluffy","Freckles","Fritz","Frizzy","Funky","Furball","Gale","Garfield","Gary","Giggles","Goopy","Graham","Grouchy","Gulliver","Gus","Hans","Harvey","Harry",
                "Hector","Huddles","Huey","J.C.","Jack","Jacques","Jake","Jazzy","Jellyroll","Jester","Jimmy","Johan","John","Johnny","Kippy","Kit","Knuckles","Lancelot","Lefty","Leo","Leonardo",
                "Leroy","Lionel","Lloyd","Lollipop","Loony","Loopy","Louie","Lucky","Mac","Max","Maxwell","Mildew","Milton","Moe","Monty","Murky","Ned","Nutty","Olaf","Orville","Oscar","Oswald",
                "Ozzie","Pancake","Peanut","Peppy","Pickles","Pierre","Pinky","Phil","Poe","Popcorn","Poppy","Presto","Reggie","Rhubarb","Ricky","Rocco","Rodney","Roger","Rollie","Romeo","Roscoe",
                "Rover","Rusty","Salty","Sammie","Scooter","Skids","Skimpy","Skip","Skipper","Skippy","Slappy","Slippy","Slumpy","Smirky","Snappy","Sniffy","Snuffy","Soupy","Spiffy","Spike","Spotty",
                "Spunky","Squeaky","Star","Stinky","Stripey","Stubby","Teddy","Tex","Tom","Tricky","Tubby","von","Wacko","Wacky","Waldo","Wally","Wesley","Whiskers","Wilbur","William","Winky","Yippie",
                "Z.Z.","Zany","Ziggy","Zilly","Zippety","Zippy","Zowie"]
                t = choice(title)
                f = choice(first)
            if gender == 'f':
                title = ["Aunt","Big","Cap'n","Captain","Colonel","Cool","Crazy","Deputy","Dippy","Doctor","Fat","Good ol'","Granny","Lady","Little","Loopy","Loud","Miss","Noisy","Princess","Prof.",
                "Queen","Sheriff","Silly","Skinny","Super","Ugly","Weird"]
                first = ["Blinky","Bongo","Bonkers","Bonnie","Boo Boo","Bouncey","Bubbles","Bumpy","C.J.","C.W.","Candy","Chirpy","Chunky","Clover","Coconut","Comet","Corky","Corny","Cranky","Crazy",
                "Cricket","Crumbly","Cuckoo","Cuddles","Curly","Daffodil","Daffy","Daphne","Dee Dee","Dinky","Dizzy","Domino","Dottie","Drippy","Droopy","Dusty","Dynamite","Fancy","Fangs","Fireball",
                "Flapjack","Flappy","Fleabag","Flip","Fluffy","Freckles","Frizzy","Furball","Ginger","Goopy","Gwen","Huddles","J.C.","Jazzy","Jellyroll","Kippy","Kit","Ladybug","Lefty","Lily","Lollipop",
                "Loony","Loopy","Lucky","Marigold","Maxie","Melody","Mildew","Mo Mo","Murky","Nutmeg","Nutty","Olive","Pancake","Peaches","Peanut","Pearl","Penny","Peppy","Petunia","Pickles","Pinky",
                "Popcorn","Poppy","Presto","Rainbow","Raven","Rhubarb","Robin","Rosie","Roxy","Sadie","Sally","Salty","Sandy","Scooter","Skids","Skimpy","Slappy","Slippy","Slumpy","Smirky","Snappy",
                "Sniffy","Snuffy","Soupy","Spiffy","Spotty","Spunky","Squeaky","Star","Stripey","Stubby","Taffy","Tricky","Trixie","Tubby","Ursula","Valentine","Vicky","Violet","von","Wacko","Wacky",
                "Whiskers","Willow","Winky","Yippie","Z.Z.","Zany","Ziggy","Zilly","Zippety","Zippy","Zowie"]
                t = choice(title)
                f = choice(first)
            last1 = ["Bagel","Banana","Bean","Beanie","Biggen","Bizzen","Blubber","Boingen","Bumber","Bumble","Bumpen","Cheezy","Crinkle","Crumble","Crunchen","Crunchy","Dandy","Dingle","Dizzen",
            "Dizzy","Doggen","Dyno","Electro","Feather","Fiddle","Fizzle","Flippen","Flipper","Frinkel","Fumble","Funny","Fuzzy","Giggle","Glitter","Google","Grumble","Gumdrop","Huckle","Hula",
            "Jabber","Jeeper","Jinx","Jumble","Kooky","Lemon","Loopen","Mac","Mc","Mega","Mizzen","Nickel","Nutty","Octo","Paddle","Pale","Pedal","Pepper","Petal","Pickle","Pinker","Poodle",
            "Poppen","Precious","Pumpkin","Purple","Rhino","Robo","Rocken","Ruffle","Smarty","Sniffle","Snorkle","Sour","Spackle","Sparkle","Squiggle","Super","Thunder","Toppen","Tricky","Tweedle",
            "Twiddle","Twinkle","Wacky","Weasel","Whisker","Whistle","Wild","Witty","Wonder","Wrinkle","Ziller","Zippen","Zooble"]
            last2 = ["batch","bee","berry","blabber","bocker","boing","boom","bop","bounce","bouncer","brains","bubble","bumble","bump","bumper","burger","butter","chomp","corn","crash","crumbs",
            "crump","crunch","dazzle","doodle","dorf","face","fidget","fink","fish","flap","flapper","flinger","flip","flipper","foot","fuddy","fussen","gabber","gadget","gargle","gloop","glop",
            "glow","goober","goose","grin","grooven","grump","hoffer","hopper","jinks","klunk","knees","loop","loose","marble","mash","masher","melon","mew","monkey","mooch","mouth","muddle",
            "muffin","mush","nerd","noodle","nose","nugget","paws","phew","phooey","pocket","poof","pop","pounce","pow","pretzel","quack","roni","scooter","screech","smirk","snooker","snoop",
            "snout","socks","speed","son","song","sparkles","speed","spinner","splat","sprinkles","sprocket","squeak","sticks","stink","swirl","tail","teeth","thud","toes","ton","toon","tooth",
            "twist","whatsit","whip","whirl","wicket","wig","wiggle","wire","woof","zaner","zap","zapper","zilla","zoom","zoop"]
            l1 = choice(last1)
            l2 = choice(last2)
            nametypes = ['titlefirst', 'first', 'titlelast', 'firstlast', 'last', 'all']
            nametype = choice(nametypes)
            if nametype == 'titlefirst':
                name = (t + " " + f)
            if nametype == 'first':
                name = (f)
            if nametype == 'firstlast':
                name = (f + " " + l1 + l2)
            if nametype == 'titlelast':
                name = (t + " " + l1 + l2)
            if nametype == 'last':
                name = (l1 + l2)
            if nametype == 'all':
                name = (t + " " + f + " " + l1 + l2)
            await ctx.channel.send("Your randomly generated name is: {}".format(name))
            print("Generated name: {}".format(name))
    @commands.command(name='makeatoon', help='Creates a random toon!')
    async def createatoon(self, ctx):
        embed = discord.Embed(title="Time to make a new toon!", description=" ", color=0xDECD9F)
        embed.set_author(name='Flippy',
        icon_url="https://i.imgur.com/XQvuCmn.png")    
        sp = ['Cat', 'Dog', 'Pig', 'Bear', 'Monkey', 'Crocodile', 'Deer', 'Mouse', 'Duck', 'Horse', 'Rabbit']
        species = choice(sp)
        embed.add_field(name="Species:", value=species)
        gend = ['Boy', 'Girl']
        gen = choice(gend)
        embed.add_field(name="Gender:", value=gen)
        gags1 = ['Toon-up', 'Trap', 'Lure', 'Sound', 'Drop']
        gags2 = ['Toon-up', 'Trap', 'Lure', 'Sound', 'Throw', 'Squirt', 'Drop']
        nogag = choice(gags1)
        orggag = choice(gags2)
        if nogag == orggag:
            nogag = choice(gags1)
            orggag = choice(gags2)
        embed.add_field(name="They will be:", value="{}less".format(nogag), inline=False)
        embed.add_field(name="They will have:", value="Organic {}".format(orggag), inline=False)
        sizes1 = ['1', '2', '3', '4']
        sizes2 = ['Long', 'Medium', 'Small']
        if species == 'Mouse':
            sizes1 = ['1', '2']
        headstyle = choice(sizes1)
        bodysize = choice(sizes2)
        legsize = choice(sizes2)
        embed.add_field(name="Head style:", value=headstyle)
        embed.add_field(name='Body size:', value=bodysize)
        embed.add_field(name='Leg size:', value=legsize)
        croll = ['full color', 'legs different', 'mixed']
        crolla = choice(croll)
        colors = ['Peach','Bright Red','Red','Maroon','Sienna','Brown','Tan','Coral','Orange','Yellow','Cream','Citrine','Lime','Sea green','Green','Light blue','Aqua','Blue','Periwinkle','Royal blue',
        'Slate blue','Purple','Lavender','Pink','Rose pink','Ice blue','Mint green','Emerald','Teal','Apricot','Amber','Crimson red','Forest green','Steel blue','Beige','Bubblegum'
        #All colors as of 12-18-2019
        ]
        if crolla == 'full color':
            fullcolor = choice(colors)
            embed.add_field(name="Toon color:", value=fullcolor)
        if crolla == 'legs different':
            headtorso = choice(colors)
            legs = choice(colors)
            embed.add_field(name="Head and torso color:", value=headtorso)
            embed.add_field(name="Leg color:", value=legs)
        if crolla == 'mixed':
            head = choice(colors)
            torso = choice(colors)
            legs = choice(colors)
            embed.add_field(name='Head color:', value=head)
            embed.add_field(name='Torso color:', value=torso)
            embed.add_field(name='Leg color:', value=legs)
        await ctx.channel.send(embed=embed)
        print("Made a new toon!")
            
    #Silly Meter Embed
    @commands.command(name='sillymeter',help='Information about the Silly Meter.')
    async def sillymeter(self, ctx):
        minfo=requests.get('https://www.toontownrewritten.com/api/sillymeter')
        data=minfo.json()
        print(data)
        embt=str()
        rs=data.get('rewards')
        potrs=rs[0]+", "+rs[1]+", and "+rs[2]
        embed=discord.Embed(title=embt,color=0xDECD9F)
        embed.set_author(name='Flippy',icon_url="https://i.imgur.com/XQvuCmn.png")
        #Active embed
        if data['state']=='Active':
            embt='The Silly Meter is Active!'
            embed.add_field(name="Silly Teams:",value=potrs)
            embed.add_field(name="Silly Progress:",value=str("{:,}".format(data['hp']))+"/5,000,000",inline=False)
        #Reward embed
        if data['state']=='Reward':
            embt='The Silly Meter is maxed out!'
            embed.add_field(name="Silly Reward:",value=data.get('winner'))
            embed.add_field(name="Previously available Silly Teams:",value=potrs,inline=False)
        #Inactive embed
        if data['state']=='Inactive':
            embt='The Silly Meter is cooling down...'
            embed.add_field(name="Upcoming Silly Teams:",value=potrs)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Toontown(bot))