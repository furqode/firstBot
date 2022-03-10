import random
import aiohttp
import hikari
import lightbulb
import requests
import alexflipnote
import akaneko
bot = lightbulb.BotApp(token='OTQ3MTY3Mzc3OTYxOTIyNjAx.YhpUXA.grrxmxc38lVP5pih6T-D5buDkBI', prefix=".", default_enabled_guilds=(925246527709020160))

# Flipnote API Client

alex_api = alexflipnote.Client()

# Event Handler
@bot.listen(hikari.StartedEvent)
async def message(event):
    print('bot has started')

# Error Handler

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.NSFWChannelOnly):
        await event.context.respond("This command can only be used in NSFW channels!")
        raise event.exception


# Ping Command

@bot.command
@lightbulb.command('ping', "says yo what's up!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("I'm aliveeee!")

#Funny Commands Group
# Joke Command

@bot.command
@lightbulb.command('joke', 'Inserts a random joke')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke_cmd(ctx):
     r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious&type=single').json()
     jokecmd = r['joke']
     await ctx.respond(jokecmd)

# Insult Command

@bot.command
@lightbulb.option('username', 'Username of the person you want to insult')
@lightbulb.command('insult', 'Insult someone by mentioning them!')
@lightbulb.implements(lightbulb.SlashCommand)
async def insult_cmd(ctx):
    r = requests.get('https://insult.mattbas.org/api/en/insult.json').json()
    insult = r['insult']
    await ctx.respond(f"{ctx.author.mention} insults {ctx.options.username}\n{insult}")


# Meme Command

@bot.command
@lightbulb.command('meme', 'Finest memes from the Internet!')
@lightbulb.implements(lightbulb.SlashCommand)
async def meme_cmd(ctx):
    r = requests.get('https://memes.blademaker.tv/api?lang=en')
    res = r.json()
    title = res["title"]
    ups = res["ups"]
    downs = res["downs"]
    sub = res["subreddit"]
    m = hikari.Embed(title=f"{title}\nSubreddit: {sub}", colour=0x79E6F3)
    m.set_image(res["image"])
    await ctx.respond(m)

# Anime Memes Command

@bot.command
@lightbulb.command('animememes', 'Memes for you Otakus')
@lightbulb.implements(lightbulb.SlashCommand)
async def animememes_cmd(ctx):
    async with aiohttp.ClientSession() as cd:
        async with cd.get("https://www.reddit.com/r/animememes.json") as r:
            animememes = await r.json()
            m = hikari.Embed(title='Memes For Otakus', colour=0x79E6F3)
            m.set_image(animememes["data"]["children"][random.randint(0,30)]["data"]["url"])
            m.set_footer(text=f"Requested by: {ctx.author}")
            await ctx.respond(m)


# SFW Stuff

# Wallpaper Command

@bot.command
@lightbulb.command('wallpaper', 'Epic Wallpapers')
@lightbulb.implements(lightbulb.SlashCommand)
async def wallpaper_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/wallpapers').json()
    wallpaper = r["image"]
    author = ctx.author
    m = hikari.Embed(title='Enjoy your Wallpaper uwu', colour=0xF37F97)
    m.set_image(wallpaper)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Smug Command

@bot.command
@lightbulb.command('smug', "You smuggin'?")
@lightbulb.implements(lightbulb.SlashCommand)
async def smug_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/smug').json()
    smug = r["image"]
    author = ctx.author.mention
    m = hikari.Embed(title= 'EVIL', description=f"{author} smugs!", colour=0xF37F97)
    m.set_image(smug)
    await ctx.respond(m)

# Dance Command

@bot.command
@lightbulb.command('dance', "Just Dance!")
@lightbulb.implements(lightbulb.SlashCommand)
async def dance_cmd(ctx):
    r = requests.get('https://purrbot.site/api/img/sfw/dance/gif').json()
    dance = r["link"]
    author = ctx.author.mention
    m = hikari.Embed(title='Dance time!', description=f"{author} dances!", colour=0xF37F97)
    m.set_image(dance)
    await ctx.respond(m)

# Smile Command

@bot.command
@lightbulb.command('smile', 'Smiling is good for health :)')
@lightbulb.implements(lightbulb.SlashCommand)
async def smile_cmd(ctx):
    r = requests.get('https://purrbot.site/api/img/sfw/smile/gif').json()
    smile = r["link"]
    author = ctx.author.mention
    m = hikari.Embed(title=':)', description=f"{author} Smiles!", colour=0xF37F97)
    m   .set_image(smile)
    await ctx.respond(m)

# Waifu Command

@bot.command
@lightbulb.command('waifu', 'Fancy an anime waifu? OwO')
@lightbulb.implements(lightbulb.SlashCommand)
async def waifu_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/waifu').json()
    waifu = r["url"]
    m = hikari.Embed(title='Waifu OwO', colour=0xF37F97)
    m.set_image(waifu)
    m.set_footer(text=f"Requested by: {ctx.author}")
    await ctx.respond(m)

# Neko Command

@bot.command
@lightbulb.command('neko', 'Anime Catgirl OwO')
@lightbulb.implements(lightbulb.SlashCommand)
async def neko_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/neko').json()
    neko = r["url"]
    author = ctx.author
    m = hikari.Embed(title='Neko OwO', colour=0xF37F97)
    m.set_image(neko)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Megumin Command

@bot.command
@lightbulb.command('megumin', 'Random Megumin Pic')
@lightbulb.implements(lightbulb.SlashCommand)
async def megumin_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/megumin').json()
    megumin = r["url"]
    author = ctx.author
    m = hikari.Embed(title='Megumin Chan! OwO', colour=0xF37F97)
    m.set_image(megumin)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Kanna Command

@bot.command
@lightbulb.command('kanna', 'Random Kanna Kamui Picture!')
@lightbulb.implements(lightbulb.SlashCommand)
async def kanna_cmd(ctx):
    r = requests.get('https://nekobot.xyz/api/image?type=kanna').json()
    kanna = r["message"]
    author = ctx.author
    m = hikari.Embed(title="Kanna Kamui OwO", colour=0xF37F97)
    m.set_image(kanna)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Shinobu Command

@bot.command
@lightbulb.command('shinobu', 'Random Shinobu Pic')
@lightbulb.implements(lightbulb.SlashCommand)
async def shinobu_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/shinobu').json()
    shinobu = r["url"]
    author = ctx.author
    m = hikari.Embed(title='Shinobu Chan! OwO', colour=0xF37F97)
    m.set_image(shinobu)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Kemonomimi Command

@bot.command
@lightbulb.command('kemonomimi', 'Anime Characters with Animal Ears and Tails!')
@lightbulb.implements(lightbulb.SlashCommand)
async def kemonomimi_cmd(ctx):
    r = requests.get('https://nekobot.xyz/api/image?type=kemonomimi').json()
    kemonomimi = r["message"]
    author = ctx.author
    m = hikari.Embed(title="OwO~", colour=0xF37F97)
    m.set_image(kemonomimi)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Food Command

@bot.command
@lightbulb.command('food', 'Random Food Pictures!')
@lightbulb.implements(lightbulb.SlashCommand)
async def food_cmd(ctx):
    r = requests.get('https://nekobot.xyz/api/image?type=food').json()
    food = r["message"]
    author = ctx.author
    m = hikari.Embed(title="Nom Nom Nom~", colour=0xF37F97)
    m.set_image(food)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)

# Awoo Command

@bot.command
@lightbulb.command('awoo', 'Random Kitsune!')
@lightbulb.implements(lightbulb.SlashCommand)
async def awoo_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/awoo').json()
    awoo = r["url"]
    author = ctx.author
    m = hikari.Embed(title='Awooga >//<', colour=0xF37F97)
    m.set_image(awoo)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)



# Laugh Command

@bot.command
@lightbulb.command('laugh', 'Have a laugh!')
@lightbulb.implements(lightbulb.SlashCommand)
async def laugh_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/laugh').json()
    laugh = r["image"]
    author = ctx.author.mention
    m = hikari.Embed(title='HAHAHA!', description=f"{author} laughs xD", colour=0xF37F97)
    m.set_image(laugh)
    await ctx.respond(m)

# Kiss Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('kiss', 'Kiss someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def kiss_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/kiss').json()
    kiss = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Kissies >.<!', description= f"{author_name} kisses {reciever_name}!", colour=0xF37F97)
    m.set_image(kiss)
    await ctx.respond(m)

# Bite Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('bite', 'Bite Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def bite_cmd(ctx):
    r = requests.get('https://purrbot.site/api/img/sfw/bite/gif').json()
    bite = r["link"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Biting :O', description= f"{author_name} bites {reciever_name}!", colour=0xF37F97)
    m.set_image(bite)
    await ctx.respond(m)

# Bonk Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('bonk', 'Bonk Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def bonk_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/bonk').json()
    bonk = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='No Horny!', description= f"{author_name} bonks {reciever_name}!", colour=0xF37F97)
    m.set_image(bonk)
    await ctx.respond(m)

# Kick Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('kick', 'Kick Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/kick').json()
    kick = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='BANG!', description= f"{author_name} kicks {reciever_name}!", colour=0xF37F97)
    m.set_image(kick)
    await ctx.respond(m)

# Bully Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('bully', 'Bully Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def bully_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/bully').json()
    bully = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Get Bullied!', description= f"{author_name} bullies {reciever_name}!", colour=0xF37F97)
    m.set_image(bully)
    await ctx.respond(m)

# Handhold Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('handhold', "Hold someone's hands!")
@lightbulb.implements(lightbulb.SlashCommand)
async def handhold_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/handhold').json()
    handhold = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='No Horny!', description= f"{author_name} holds {reciever_name}'s hands!", colour=0xF37F97)
    m.set_image(handhold)
    await ctx.respond(m)

# Highfive Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('highfive', 'Give someone a highfive!')
@lightbulb.implements(lightbulb.SlashCommand)
async def highfive_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/highfive').json()
    highfive = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='No Horny!', description= f"{author_name} gives {reciever_name} a highfive!", colour=0xF37F97)
    m.set_image(highfive)
    await ctx.respond(m)

# Yeet Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('yeet', 'Yeet Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def yeet_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/yeet').json()
    yeet = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Get Yeeted!', description= f"{author_name} yeets {reciever_name}!", colour=0xF37F97)
    m.set_image(yeet)
    await ctx.respond(m)

# Tackle Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('tackle', 'Tackle Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def tackle_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/glomp').json()
    tackle = r["url"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='No Horny!', description= f"{author_name} tackles {reciever_name}!", colour=0xF37F97)
    m.set_image(tackle)
    await ctx.respond(m)

# Tickle Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('tickle', 'Tickle Someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def tickle_cmd(ctx):
    r = requests.get('https://purrbot.site/api/img/sfw/tickle/gif').json()
    tickle = r["link"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Tickling >///<!', description= f"{author_name} tickles {reciever_name}!",colour=0xF37F97)
    m.set_image(tickle)
    await ctx.respond(m)

# Cry Command

@bot.command
@lightbulb.command('cry', 'Do you want to cry?')
@lightbulb.implements(lightbulb.SlashCommand)
async def cry_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/cry').json()
    cry = r["image"]
    author = ctx.author.mention
    m = hikari.Embed(title=':(', description=f"{author} cries :c", colour=0xF37F97)
    m.set_image(cry)
    await ctx.respond(m)

# Cringe Command

@bot.command
@lightbulb.command('cringe', 'Ewww')
@lightbulb.implements(lightbulb.SlashCommand)
async def cringe_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/cringe').json()
    cringe = r["url"]
    author = ctx.author.mention
    m = hikari.Embed(title='EWWW', description=f"{author} is cringing rn", colour=0xF37F97)
    m.set_image(cringe)
    await ctx.respond(m)

# Blush Command

@bot.command
@lightbulb.command('blush', '>///<')
@lightbulb.implements(lightbulb.SlashCommand)
async def blush_cmd(ctx):
    r = requests.get('https://api.waifu.pics/sfw/blush').json()
    blush = r["url"]
    author = ctx.author.mention
    m = hikari.Embed(title='>///<', description=f"{author} blushes >.<", colour=0xF37F97)
    m.set_image(blush)
    await ctx.respond(m)

# Hug Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('hug', 'Give someone a hug')
@lightbulb.implements(lightbulb.SlashCommand)
async def hug_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/hug').json()
    hug = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Huggies!', description= f"{author_name} hugs {reciever_name}!", colour=0xF37F97)
    m.set_image(hug)
    await ctx.respond(m)

# Pat Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('pat', 'Pat someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def pat_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/pat').json()
    pat = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Pat Pat!', description= f"{author_name} pats {reciever_name}!", colour=0xF37F97)
    m.set_image(pat)
    await ctx.respond(m)

# Cuddle Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('cuddle', 'Cuddle someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cuddle_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/cuddle').json()
    cuddle = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Cuddles!', description= f"{author_name} cuddles {reciever_name}!", colour=0xF37F97)
    m.set_image(cuddle)
    await ctx.respond(m)

# Lick Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('lick', 'Lick someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def lick_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/lick').json()
    lick = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='>////<', description= f"{author_name} licks {reciever_name}!", colour=0xF37F97)
    m.set_image(lick)
    await ctx.respond(m)

# Slap Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('slap', 'Wanna slap someone?')
@lightbulb.implements(lightbulb.SlashCommand)
async def slap_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/slap').json()
    slap = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Violence!', description=f"{author_name} slaps {reciever_name}!", colour=0xF37F97)
    m.set_image(slap)
    await ctx.respond(m)

# Poke Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('poke', 'Senpai notice meeeee!')
@lightbulb.implements(lightbulb.SlashCommand)
async def poke_cmd(ctx):
    r = requests.get('http://api.nekos.fun:8080/api/poke').json()
    poke = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='Pokey Pokey uwu', description=f"{author_name} pokes {reciever_name}!", colour=0xF37F97)
    m.set_image(poke)
    await ctx.respond(m)

# Feed Command

@bot.command
@lightbulb.option('name', 'Name of the user', type=hikari.User)
@lightbulb.command('feed', 'Feed someone!')
@lightbulb.implements(lightbulb.SlashCommand)
async def feed_cmd(ctx):
    r = requests.get('	http://api.nekos.fun:8080/api/feed').json()
    feed = r["image"]
    author_name = ctx.author.mention
    reciever_name = ctx.options.name.mention
    m = hikari.Embed(title='FOOD!!', description=f"{author_name} feeds {reciever_name}! Yummy :c", colour=0xF37F97)
    m.set_image(feed)
    await ctx.respond(m)


# Rating Commands
# Cool Rate Command

@bot.command
@lightbulb.command('coolrate', "Check how cool you are!")
@lightbulb.implements(lightbulb.SlashCommand)
async def cr_cmd(ctx):
    author = ctx.author.mention
    m = hikari.Embed(title='Cool Rating', description=f"You are {random.randrange(101)}% Cool! {author}", colour=0x5ADECD)
    await ctx.respond(m)

# Gay Rate Command

@bot.command
@lightbulb.option('username', 'Username of the person you want to check the Gayrate of', type=hikari.User)
@lightbulb.command('gay', "Check how gay someone is!")
@lightbulb.implements(lightbulb.SlashCommand)
async def gay_cmd(ctx):
    reciever = ctx.options.username.mention
    m = hikari.Embed(title='Gay Rating', description=f"{reciever} is {random.randrange(101)}% Gay!", colour=0x5ADECD)
    await ctx.respond(m)

# Simp Rate Command

@bot.command
@lightbulb.option('username', 'Username of the person you want to check SimpRate of', type=hikari.User)
@lightbulb.command('simp', 'Check how much of a simp someone is!')
@lightbulb.implements(lightbulb.SlashCommand)
async def simp_cmd(ctx):
    reciever = ctx.options.username.mention
    m = hikari.Embed(title='Simp Rating', description=f"{reciever} is {random.randrange(101)}% simp!", colour=0x5ADECD)
    await ctx.respond(m)


# Sad Cat Command 

@bot.command
@lightbulb.command('sadcat', 'A sad cat for you :(')
@lightbulb.implements(lightbulb.SlashCommand)
async def sad_cat(ctx):
    r = await alex_api.sadcat()
    m = hikari.Embed(title='Sad Kitty', colour=0xF37F97)
    author = ctx.author
    m.set_image(r)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)
    await alex_api.close()

# Random Cat Command

@bot.command
@lightbulb.command('cat', 'Cute cat pic for you')
@lightbulb.implements(lightbulb.SlashCommand)
async def cats_cmd(ctx):
    r = await alex_api.cats()
    m = hikari.Embed(title='Kitty Cat!', colour=0xF37F97)
    author = ctx.author
    m.set_image(r)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)
    await alex_api.close()

# Random Birb Command

@bot.command
@lightbulb.command('birb', "Cute 'birb' for you")
@lightbulb.implements(lightbulb.SlashCommand)
async def birb_cmd(ctx):
    r = await alex_api.birb()
    m = hikari.Embed(title="It's a birb!", colour=0xF37F97)
    author = ctx.author
    m.set_image(r)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)
    await alex_api.close()

# Coffee Picture Command

@bot.command
@lightbulb.command('coffee', 'Fancy a cup of coffee?')
@lightbulb.implements(lightbulb.SlashCommand)
async def coffee_cmd(ctx):
    r = await alex_api.coffee()
    m = hikari.Embed(title="Here's your cup of coffee!", colour=0xF37F97)
    author = ctx.author
    m.set_image(r)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)
    await alex_api.close()

# Random Dog Command

@bot.command
@lightbulb.command('dog', 'Cute Doggo for you')
@lightbulb.implements(lightbulb.SlashCommand)
async def dog_cmd(ctx):
    r = await alex_api.dogs()
    m = hikari.Embed(title="Cute Doggie!", colour=0xF37F97)
    author = ctx.author
    m.set_image(r)
    m.set_footer(text=f"Requested by: {author}")
    await ctx.respond(m)
    await alex_api.close()

# EMOJIFY STUFF COMMANDS
# Emojify Command

# @bot.command
# @lightbulb.command('emojify', 'Turn your text into emojis')
# @lightbulb.implements(lightbulb.PrefixCommand)
# async def emojify_cmd(ctx,*,text):
#     emojis = []
#     for s in text:
#         if s.isdecimal():
#             num2emo = {'0':'zero','1':'one','2':'two', '3':'three', '4':'four', '5':'five' , '6':'six', '7':'seven','8':'eight', '9':'nine'}
#             emojis.append(f":{num2emo.get(s)}:")
#         elif s.isalpha():
#             emojis.append(f":regional_indicator_{s}:")
#         else:
#             emojis.append(s)
#     await ctx.respond(' '.join(emojis))




    

# Grouping

@bot.command
@lightbulb.command('group', 'my group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcmd', 'a sub command')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('Now that is a Sub Command')

# Options for commands

@bot.command
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.option('num2', 'Second number', type=int)
# Options must always be above lightbulb.command 
@lightbulb.command('add', 'Adds two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

# Help Command

# HELP_MESSAGE = """
# Commands Available:
# /ping - Ping the bot and it will respond!
# /add - Adds two numbers together!
# /joke - Inserts a random joke!
# /meme - Inserts a random meme from the Internet!
# /animememes - Inserts a random Anime Meme from r/animememes Subreddit!
# /sadcat - Inserts a random sad cat pic or gif!
# /cat - Inserts a random cat pic or gif1
# /dog - Inserts a random dog pic or gif!
# /birb - Inserts a random birb pic or gif!
# /coffee - Inserts a random coffee pic!
# /neko - Inserts a random neko pic!
# /waifu - Inserts a random anime waifu pic!
# /megumin - Inserts a random Megumin Chan pic!
# /shinobu - Inserts a random Shinobu Chan pic!
# /awoo - Inserts a random Kitsune pic!
# /smug - Inserts a random smug pic or gif!
# /cry - Inserts a random crying pic or gif!
# /dance - Inserts a random dancing gif!
# /smile - Inserts a random smiling gif!
# /cringe - Inserts a random cringing gif!
# /blush - Inserts a random blushing gif!
# /kiss - Kiss someone!
# /hug - Hug someone!
# /cuddle - Cuddle someone!
# /lick - Lick someone!
# /pat - Pat someone!
# /slap - Slap someone!
# /poke - Poke someone!
# /tickle - Tickle someone!
# /bite - Bite someone!
# /bonk - Bonk someone!
# /yeet - Yeet someone!
# /bully - Bully someone!
# /tackle - Tackle someone!
# /kick - Kick someone! (gif image)
# /handhold - Hold someone's hand!
# /highfive - Give someone a highfive!
# /wallpaper - Epic Wallpapers!


# Rating Commands:
# /coolrate - Check how cool you are!
# /gay - Check how gay someone is!
# /simp - Check how much of a Simp someone is!



# @bot.command
# @lightbulb.command('help', 'help command')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def help(ctx):
#     embed = hikari.Embed(
#         title='Commands List',
#         description=f"{HELP_MESSAGE}"
#         )
#     await ctx.respond(embed)

# Testing Help Command

@bot.command
@lightbulb.command('help', "Commands available for Twizzy Bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def help_group(ctx):
    m = hikari.Embed(title="Help", description="Use / Prefix for all the commands", colour=0xC574DD)
    m.add_field(name='😄 Fun', value="hug, kiss, cuddle, slap, dance, smug, awoo, blush, smile, cringe, cry, lick, pat, poke, tickle, bite, bonk, yeet, bully, tackle, kick, handhold, highfive")
    m.add_field(name='🖼️ Images',value="wallpaper, cat, sadcat, dog, birb, coffee, food, neko, kemonomimi, waifu, megumin, kanna, shinobu")
    m.add_field(name='😂 Funny',value="joke, insult, memes, animememes")
    m.add_field(name='⭐ Rating',value="coolrate, gay, simp")
    await ctx.respond(m)
    

bot.run()

