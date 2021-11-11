import random
from random import *
import discord
from discord.ext import commands

class MonHun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Monster Hunter World specific commands
    @commands.command(name='mhw',help='Multicommand related to monster hunter world specifically.')
    async def mhw(self, ctx, cmd=''):
        cmds=['locale','hunt']
        
        #Locales
        if cmd=='locale':
            locales = ['Ancient Forest', 'Wildspire Waste', 'Coral Highlands', 'Rotten Vale', 'Everstream', 'Confluence of Fates', 'Hoarfrost Reach', 'Caverns of El Dorado', 
            'Guiding Lands', 'Secluded Valley', 'Origin Isle', 'Castle Schrade', 'Seliana Supply Cache']
            chosen = choice(locales)
            print('Chosen locale: {}'.format(chosen))
            embed = discord.Embed(title="Let's go somewhere!", description="Let's visit the {}!".format(chosen), color=0x771c85)
            embed.set_author(name='Palico',
            icon_url="https://i.imgur.com/DLiK3dA.png")
            if chosen == 'Ancient Forest':
                embed.set_image(url='https://i.imgur.com/MCgyIbJ.jpg')
            if chosen == 'Wildspire Waste':
                embed.set_image(url='https://i.imgur.com/C5OlxhP.jpg')
            if chosen == 'Coral Highlands':
                embed.set_image(url='https://i.imgur.com/8HqSMZE.jpg')
            if chosen == 'Rotten Vale':
                embed.set_image(url='https://i.imgur.com/5J4x8GN.jpg')
            if chosen == 'Everstream':
                embed.set_image(url='https://i.imgur.com/dTYVyqD.png')
            if chosen == 'Confluence of Fates':
                embed.set_image(url='https://i.imgur.com/clsZUUS.jpg')
            if chosen == 'Hoarfrost Reach':
                embed.set_image(url='https://i.imgur.com/n3HddqE.jpg')
            if chosen == 'Caverns of El Dorado':
                embed.set_image(url='https://i.imgur.com/7eWqB6h.jpg')
            if chosen == 'Guiding Lands':
                embed.set_image(url='https://i.imgur.com/A1YWq8o.jpg')
            if chosen == 'Secluded Valley':
                embed.set_image(url='https://i.imgur.com/8DYLZFD.jpg')
            if chosen == 'Origin Isle':
                embed.set_image(url="https://i.imgur.com/Nt5mmOP.png")
            if chosen == 'Castle Schrade':
                embed.set_image(url='https://static.wikia.nocookie.net/monsterhunter/images/6/60/MHWI-Fatalis_Screenshot_016.jpg')
            if chosen=='Seliana Supply Cache':
                embed.set_image(url='https://i.imgur.com/aasjLop.png')
            await ctx.channel.send(embed=embed)
            
        #Specific monster hunt
        if cmd=='hunt':
            embed = discord.Embed(title="Wanna fight a meownster?", description="Your meownster is:", color=0x771c85)
            embed.set_author(name='Palico',
        icon_url="https://i.imgur.com/DLiK3dA.png")
            all_images = ["https://i.imgur.com/sWJGHF1.png", #Zinogre,
            "https://i.imgur.com/eppblI5.png", #Yian Garuga
            "https://i.imgur.com/IBR4DNn.png", #Banbaro
            "https://i.imgur.com/WGeJmw6.png", #Tigrex
            "https://i.imgur.com/5xoop0G.png", #Rajang
            "https://i.imgur.com/TKog8EJ.png", #Deviljho
            "https://i.imgur.com/N2T9r5D.png", #Odogaron
            "https://i.imgur.com/5tbvqVK.png", #Acidic Glavenus
            "https://i.imgur.com/M2uNBbe.png", #Anjanath
            "https://i.imgur.com/CJnvuiz.png", #Azure Rathalos
            "https://i.imgur.com/xKBE6Dj.png", #Barioth
            "https://i.imgur.com/p1npCfR.png", #Barroth
            "https://i.imgur.com/zDzsYZl.png", #Bazelgeuse
            "https://i.imgur.com/aQIlazX.png", #Beotodus
            "https://i.imgur.com/ja2QZuH.png", #Black Diablos
            "https://i.imgur.com/oSFpnR5.png", #Blackveil Vaal Hazak
            "https://i.imgur.com/yx4l5NQ.png", #Brachydios
            "https://i.imgur.com/2v67kV0.png", #Brute Tigrex
            "https://i.imgur.com/HUVAFXa.png", #Coral Pukei-Pukei
            "https://i.imgur.com/3hogwHZ.png", #Diablos
            "https://i.imgur.com/bLW8Oxi.png", #Dodogama
            "https://i.imgur.com/VQnT3FN.png", #Ebony Odogaron
            "https://i.imgur.com/wq52tcg.png", #Fulgur Anjanath
            "https://i.imgur.com/CwyKuUG.png", #Glavenus
            "https://i.imgur.com/HAex2iE.png", #Gold Rathian
            "https://i.imgur.com/8CSUXZn.png", #Great Girros
            "https://i.imgur.com/Ngbsqiu.png", #Great Jagras
            "https://i.imgur.com/X4vVQP1.png", #Jyuratodus
            "https://i.imgur.com/Mm5l6hz.png", #Kirin
            "https://i.imgur.com/1eUUiqU.png", #Kulu Ya-Ku
            "https://i.imgur.com/nyO86fR.png", #Kulve Taroth
            "https://i.imgur.com/aLn7mZf.png", #Kushala Daora
            "https://i.imgur.com/WoF63sQ.png", #Lavasioth
            "https://i.imgur.com/2dRWCna.png", #Legiana
            "https://i.imgur.com/MPcBrPt.png", #Lunastra
            "https://i.imgur.com/fC6RX57.png", #Namielle
            "https://i.imgur.com/6BtWHJv.png", #Nargacuga
            "https://i.imgur.com/6XX17Br.png", #Nergigante
            "https://i.imgur.com/1AYC5mU.png", #Nightshade Paolumu
            "https://i.imgur.com/knFSYkz.png", #Paolumu
            "https://i.imgur.com/1ex73Sd.png", #Pink Rathian
            "https://i.imgur.com/mJ3x9Kp.png", #Pukei-Pukei
            "https://i.imgur.com/Z6C5k91.png", #Radobaan
            "https://i.imgur.com/TUvW8lb.png", #Rathalos
            "https://i.imgur.com/RuJyy2r.png", #Rathian
            "https://i.imgur.com/Stjv833.png", #Ruiner Nergigante
            "https://i.imgur.com/Cdr8jcE.png", #Safi'Jiiva
            "https://i.imgur.com/aZmNfFx.png", #Savage Deviljho
            "https://i.imgur.com/cADIsUb.png", #Scarred Yian Garuga
            "https://i.imgur.com/3qNP6NZ.png", #Seething Bazelgeuse
            "https://i.imgur.com/XsoYYRi.png", #Shara Ishvalda
            "https://i.imgur.com/46XlpZS.png", #Shrieking Legiana
            "https://i.imgur.com/oYNEyoe.png", #Silver Rathalos
            "https://i.imgur.com/ozZoa8v.png", #Stygian Zinogre
            "https://i.imgur.com/6FkyvQj.png", #Teostra
            "https://i.imgur.com/PkwrvzT.png", #Tobi-Kadachi
            "https://i.imgur.com/hxxqCxz.png", #Tzitzi Ya-Ku
            "https://i.imgur.com/3eZtmuH.png", #Urugaan
            "https://i.imgur.com/Q2cS7R4.png", #Vaal Hazak
            "https://i.imgur.com/fQCjbGm.png", #Velkhana
            "https://i.imgur.com/6mT3ILQ.png", #Viper Tobi-Kadachi
            "https://i.imgur.com/qrPSToa.png", #Xeno'Jiiva
            "https://i.imgur.com/MhIu77b.png", #Zorah Magdaros
            "https://vignette.wikia.nocookie.net/monsterhunter/images/6/6d/MHWI-Alatreon_Icon.png", #Alatreon
            "https://vignette.wikia.nocookie.net/monsterhunter/images/6/6a/MHWI-Furious_Rajang_Icon.png", #Furious Rajang
            "https://vignette.wikia.nocookie.net/monsterhunter/images/6/68/MHWI-Raging_Brachydios_Icon.png", #Raging Brachydios
            "https://static.wikia.nocookie.net/monsterhunter/images/0/09/MHWI-Fatalis_Icon.png" #Fatalis
            ]
            chosen = choice(all_images)
            embed.set_image(url=chosen)
            print("Randmonster chose {}".format(chosen))
            await ctx.channel.send(embed=embed)
            
        #Handling other responses.
        if cmd not in cmds:
            await ctx.channel.send("This MHW command does not exist.")
            
    #MH Rise commands
    @commands.command(name='mhr', help='Monster Hunter Rise commands')
    async def mhr(self, ctx, cmd=''):
        cmds=['locale','party','hunt']
        
        #Locales
        if cmd=='locale':
            locales = ['Shrine Ruins','Flooded Forest','Stronghold','Frost Islands','Sandy Plains','Lava Caverns']
            chosen = choice(locales)
            print('Chosen locale: {}'.format(chosen))
            embed = discord.Embed(title="Not sure where to go?", description="Why not check out the {}?".format(chosen), color=0x771c85)
            embed.set_author(name='Minoto',
            icon_url="https://i.imgur.com/1VL0fRA.png")
            if chosen == 'Shrine Ruins':
                embed.set_image(url='https://i.imgur.com/vFqdU8v.jpg')
            if chosen == 'Flooded Forest':
                embed.set_image(url='https://i.imgur.com/ThkcYN6.jpg')
            if chosen=='Stronghold':
                embed.set_image(url='https://i.imgur.com/3J00Jv7.jpg')
            if chosen == 'Frost Islands':
                embed.set_image(url='https://i.imgur.com/pfMHs0f.jpg')
            if chosen == 'Sandy Plains':
                embed.set_image(url='https://i.imgur.com/dNn54Am.jpg')
            if chosen== 'Lava Caverns':
                embed.set_image(url='https://i.imgur.com/jCnTHzm.jpg')
            await ctx.channel.send(embed=embed)
        
        #Party composition
        if cmd=='party':
            parties=['two palicos','two palamutes','one palico and one palamute','solo','one palico','one palamute']
            chosen=choice(parties)
            if chosen=='solo':
                print("Someone got a solo challenge, uh oh!")
                await ctx.channel.send("Up for a challenge? Why not try to solo your next quest?")
            else:
                print("Someone was told to bring {} on their next quest.".format(chosen))
                await ctx.channel.send("You should bring {} on your next quest!".format(chosen))
                
        #MHRise Hunts
        if cmd=='hunt':
            embed = discord.Embed(title="Wanna fight a meownster?", description="Your meownster is:", color=0x771c85)
            embed.set_author(name='Palico',
        icon_url="https://i.imgur.com/DLiK3dA.png")
            all_images = [#Base roster
            "https://static.wikia.nocookie.net/monsterhunter/images/c/cf/MHRise-Aknosom_Icon.png", #Aknosom
            "https://static.wikia.nocookie.net/monsterhunter/images/9/9e/MHRise-Almudron_Icon.png", #Almudron
            "https://static.wikia.nocookie.net/monsterhunter/images/7/76/MHRise-Anjanath_Icon.png", #Anjanath
            "https://static.wikia.nocookie.net/monsterhunter/images/9/95/MHRise-Arzuros_Icon.png", #Arzuros
            "https://static.wikia.nocookie.net/monsterhunter/images/f/ff/MHRise-Barioth_Icon.png", #Barioth
            "https://static.wikia.nocookie.net/monsterhunter/images/6/69/MHRise-Barroth_Icon.png", #Barroth
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f4/MHRise-Basarios_Icon.png", #Basarios 
            "https://static.wikia.nocookie.net/monsterhunter/images/4/4d/MHRise-Bishaten_Icon.png", #Bishaten
            "https://static.wikia.nocookie.net/monsterhunter/images/5/54/MHRise-Diablos_Icon.png", #Diablos
            "https://static.wikia.nocookie.net/monsterhunter/images/e/e0/MHRise-Goss_Harag_Icon.png", #Goss Harag
            "https://static.wikia.nocookie.net/monsterhunter/images/9/9d/MHRise-Great_Baggi_Icon.png", #Great Baggi
            "https://static.wikia.nocookie.net/monsterhunter/images/1/12/MHRise-Great_Izuchi_Icon.png", #Great Izuchi
            "https://static.wikia.nocookie.net/monsterhunter/images/7/71/MHRise-Great_Wroggi_Icon.png", #Great Wroggi
            "https://static.wikia.nocookie.net/monsterhunter/images/8/83/MHRise-Jyuratodus_Icon.png", #Jyuratodus
            "https://static.wikia.nocookie.net/monsterhunter/images/d/dc/MHRise-Khezu_Icon.png", #Khezu 
            "https://static.wikia.nocookie.net/monsterhunter/images/b/b0/MHRise-Kulu-Ya-Ku_Icon.png", #Kulu
            "https://static.wikia.nocookie.net/monsterhunter/images/b/bb/MHRise-Lagombi_Icon.png", #Lagombi 
            "https://static.wikia.nocookie.net/monsterhunter/images/a/a6/MHRise-Magnamalo_Icon.png", #Magnamalo 
            "https://static.wikia.nocookie.net/monsterhunter/images/2/20/MHRise-Mizutsune_Icon.png", #Mizutsune
            "https://static.wikia.nocookie.net/monsterhunter/images/4/46/MHRise-Nargacuga_Icon.png", #Nargacuga
            "https://static.wikia.nocookie.net/monsterhunter/images/a/a3/MHRise-Pukei-Pukei_Icon.png", #Pukei-Pukei
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f3/MHRise-Rajang_Icon.png", #Rajang
            "https://static.wikia.nocookie.net/monsterhunter/images/6/6e/MHRise-Rakna-Kadaki_Icon.png", #Rakna-Kadaki 
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f5/MHRise-Rathalos_Icon.png", #Rathalos
            "https://static.wikia.nocookie.net/monsterhunter/images/e/e6/MHRise-Rathian_Icon.png", #Rathian
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f2/MHRise-Royal_Ludroth_Icon.png", #Royal Ludroth
            "https://static.wikia.nocookie.net/monsterhunter/images/6/62/MHRise-Somnacanth_Icon.png", #Somnacanth 
            "https://static.wikia.nocookie.net/monsterhunter/images/b/ba/MHRise-Tetranadon_Icon.png", #Tetranadon 
            "https://static.wikia.nocookie.net/monsterhunter/images/b/b7/MHRise-Tigrex_Icon.png", #Tigrex
            "https://static.wikia.nocookie.net/monsterhunter/images/e/eb/MHRise-Tobi-Kadachi_Icon.png", #Tobi-Kadachi
            "https://static.wikia.nocookie.net/monsterhunter/images/7/7a/MHRise-Volvidon_Icon.png", #Volvidon 
            "https://static.wikia.nocookie.net/monsterhunter/images/6/64/MHRise-Zinogre_Icon.png", #Zinogre
            "https://static.wikia.nocookie.net/monsterhunter/images/9/9d/MHRise-Thunder_Serpent_Narwa_Icon.png", #Thunder Serpent Narwa
            "https://static.wikia.nocookie.net/monsterhunter/images/e/eb/MHRise-Wind_Serpent_Ibushi_Icon.png", #Wind Serpent Ibushi
            "https://static.wikia.nocookie.net/monsterhunter/images/4/48/MHRise-Apex_Mizutsune_Icon.png", #Apex Mizutsune
            "https://static.wikia.nocookie.net/monsterhunter/images/5/5f/MHRise-Apex_Rathian_Icon.png", #Apex Rathian
            "https://static.wikia.nocookie.net/monsterhunter/images/3/36/MHRise-Apex_Arzuros_Icon.png", #Apex Arzuros
            #TU1
            "https://static.wikia.nocookie.net/monsterhunter/images/7/7b/MHRise-Chameleos_Icon.png", #Chameleos
            "https://static.wikia.nocookie.net/monsterhunter/images/5/5b/MHRise-Kushala_Daora_Icon.png", #Kushala Daora
            "https://static.wikia.nocookie.net/monsterhunter/images/3/35/MHRise-Teostra_Icon.png", #Teostra
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f5/MHRise-Bazelgeuse_Icon.png", #Bazelgeuse
            "https://static.wikia.nocookie.net/monsterhunter/images/1/18/MHRise-Apex_Rathalos_Icon.png", #Apex Rathalos
            "https://static.wikia.nocookie.net/monsterhunter/images/b/b0/MHRise-Apex_Diablos_Icon.png", #Apex Diablos
            #TU2
            "https://static.wikia.nocookie.net/monsterhunter/images/f/f7/MHRise-Apex_Zinogre_Icon.png", #Apex Zinogre
            "https://static.wikia.nocookie.net/monsterhunter/images/8/88/MHRise-Crimson_Glow_Valstrax_Icon.png", #Crimson Glow Valstrax
            "https://static.wikia.nocookie.net/monsterhunter/images/4/4e/MHRise-Narwa_the_Allmother_Icon.png" #Narwa the Allmother
            ]
            chosen = choice(all_images)
            embed.set_image(url=chosen)
            print("Randmonster chose {}".format(chosen))
            await ctx.channel.send(embed=embed)
        
        #Handling other responses.
        if cmd not in cmds:
            await ctx.channel.send("This MHR command does not exist.")
            
    #Weapon Choice
    @commands.command(name='mhweapon', help='Chooses a random weapon from Monster Hunter.')
    async def mhweapon(self, ctx):
        weaponlist = ['Sword and Shield!<:sns:657013172732952576>', 'Dual Blades!<:db:657012868285333534>', 'Greatsword!<:gs:657012887239393280>', 'Longsword!<:ls:657013124423221248>',
        'Hammer!<:hm:657012981556838410>', 'Bow!<:mhbow:657012914477203467>', 'Light Bowgun!<:lbg:657013097537732625>', 'Heavy Bowgun!<:hbg:657013016570888221>',
        'Hunting Horn!<:hh:657013036183191582>', 'Lance!<:l_:657013076448641058>', 'Gunlance!<:gl:657012959154798650>', 'Insect Glaive!<:ig:657013054713757718>', 'Chargeblade!<:cb:657012935671152690>',
        'Switchaxe!<:sax:657013157570674698>']
        weapon = choice(weaponlist)
        print("mhweapon chooses {}!".format(weapon))
        await ctx.channel.send("You should use {}".format(weapon))
    
def setup(bot):
    bot.add_cog(MonHun(bot))