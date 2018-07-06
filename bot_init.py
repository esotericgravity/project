import discord
from discord.ext import commands
import numpy
import os
import gunicorn
import r6sapi
import apiclient
import asyncio


pref = "!"
bot = commands.Bot(command_prefix=pref)
r6auth = r6sapi.Auth(r6email, r6pwd)

def init_b(b):
    a='board:\n\n'
    a += '       |       |       '
    a+='\n  ' + b[6] + '  |' + '  ' + b[7] + '  |'+ '   ' + b[8] + '   '
    a+='\n       |       |       '
    a+='\n---------------'
    a += '\n       |       |       '
    a+='\n  ' + b[3] + '  |' + '  ' + b[4] + '  |'+ '   ' + b[5] + '   '
    a+='\n       |       |       '
    a+='\n---------------'
    a += '\n       |       |       '
    a+='\n  ' + b[0] + '  |' + '  ' + b[1] + '  |'+ '   ' + b[2] + '   '
    a+='\n       |       |       '
    a+='\n'
    checkb(b)
    return a

def checkb(b):
    if((b[7-1]== 'O' and b[8-1]=='O' and b[9-1]=='O') or
               (b[4-1]== 'O' and b[5-1]=='O' and b[6-1]=='O') or
               (b[1-1]== 'O' and b[2-1]=='O' and b[3-1]=='O') or
               (b[1-1]== 'O' and b[4-1]=='O' and b[7-1]=='O') or
               (b[2-1]== 'O' and b[5-1]=='O' and b[8-1]=='O') or
               (b[3-1]== 'O' and b[6-1]=='O' and b[9-1]=='O') or
               (b[1-1]== 'O' and b[5-1]=='O' and b[9-1]=='O') or
               (b[3-1]== 'O' and b[5-1]=='O' and b[7-1]=='O')):
        return 1
    elif((b[7-1]== 'X' and b[8-1]=='X' and b[9-1]=='X') or
               (b[4-1]== 'X' and b[5-1]=='X' and b[6-1]=='X') or
               (b[1-1]== 'X' and b[2-1]=='X' and b[3-1]=='X') or
               (b[1-1]== 'X' and b[4-1]=='X' and b[7-1]=='X') or
               (b[2-1]== 'X' and b[5-1]=='X' and b[8-1]=='X') or
               (b[3-1]== 'X' and b[6-1]=='X' and b[9-1]=='X') or
               (b[1-1]== 'X' and b[5-1]=='X' and b[9-1]=='X') or
               (b[3-1]== 'X' and b[5-1]=='X' and b[7-1]=='X')):
        return 2
    else:
        return 0
def input(b,s):
    b[int(s[2])-1]=s[0].upper()

@bot.event
async def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    t= time.time()
    await ctx.send('pinging...')
    p = time.time()- t
    await ctx.send('{} ms'.format(p))

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

# @bot.command()
# async def yt(ctx, a):
#     await ctx.send('searching for {}...'.format(a))
#     await ctx.send()

@bot.command()
@asyncio.coroutine
def r6(ctx, a, b=""):
    p=None
    if ctx.message.author.name == "Semper_Gumby":
        yield from ctx.channel.send('shut up ' + ctx.message.author.name + ', ur a')
    try:
        p= yield from r6auth.get_player(a, r6sapi.Platforms.UPLAY)
    except:
        yield from ctx.channel.send('player not found')
    p.load_gamemodes()
    o = yield from p.load_weapons()
    op = p.load_all_operators()
    # yield from ctx.channel.send(str(o.kills))
    a=""
    f=" "
    for i in o:
        a+=('weapon: {}\t\t\t\t\tkill count: {}\t\t\t\t\theadshot count: {}\t\t\t\t\taccuracy: {}%\n'.format(i.name,i.kills,i.headshots, i.hits/i.shots*100))
        # yield (i.name, i.kills,i.headshots,i.hits/i.shots*100)
    yield from bot.wait_until_ready()
    yield from ctx.channel.send(a)
    # if b!="":
    #     for i in op:
    #         if i ==b:
    #             w=p.get_operator(i)
    #             f+=("{} stats:\nwins: {}\t\t\t\t\tkill count: {}\t\t\t\t\tdeath count: {}\t\t\t\t\theadshot count: {}\t\t\t\t\tmelees: {}\t\t\t\t\ttime played: {}".format(w.name,w.wins,w.kills,w.deaths,w.headshots, w.melees,w.time_played))
    #     yield from ctx.channel.send(f)
# asyncio.get_event_loop().run_until_complete(r6())

@bot.command()
async def tictactoe(ctx):
    b = True
    c = 0
    if ctx.message.author.name == "Semper_Gumby":
        await ctx.send('shut up ' + ctx.message.author.name + ', ur a ')
    else:
        await ctx.send('X or O?')
        msg = await bot.wait_for("message")
        x=ctx.message.author
        y= msg.author
        x=x.name
        y=y.name
        if msg.content=='X':
            await ctx.send(x + ' will play O and ' + y+ ' will play X')
        elif msg.content=='O':
            await ctx.send(x + ' will play X and ' + y+ ' will play O')

        if numpy.random.randint(0, 1) == 0:
            await ctx.send(y +' will go first')
            b = False
        else:
            await ctx.send(x + ' will go first')
        b = ['   ','   ','   ','   ','   ','   ','   ','   ', '   ']
        await ctx.send('enter moves in the format: {X/O} {1-9}')
        await ctx.send('1-9 correspond to the 9 spots on a tictactoe board')
        await ctx.send('for example, 1 = bottom left, 5 = middle, and 9 = top right')
        await ctx.send(init_b(b))
        while (checkb(b)==0):
            try:
                g = await bot.wait_for("message")
                input(b,g.content)
            except ValueError:
                g = await bot.wait_for("message")
                input(b,g.content)
            c+=1
            if c == 9:
                await ctx.send('tie game\ngame over')
            try:
                h = await bot.wait_for("message")
                input(b,h.content)
            except ValueError:
                h = await bot.wait_for("message")
                input(b,h.content)
            #await ctx.send('verify')
            c+=1
            await ctx.send(init_b(b))
            if(checkb(b)==1):
                await ctx.send('O wins')
            elif(checkb(b)==2):
                await ctx.send('X wins')
        await ctx.send('game over')

bot.run(token)
