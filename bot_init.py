import discord
from discord.ext import commands
import numpy
import os
import asyncio
import time
import spotipy
import spotipy.util as util

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
async def clear(ctx):
    m=[]
    async for i in ctx.channel.history(limit=1000):
        m.append(i)
    for i in m:
        if i.author==bot.user:
            await bot.http.delete_message(ctx.channel.id, i.id)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def tictactoe(ctx):
    b = True
    c = 0
    if ctx.message.author.name == "temp":
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

@bot.command()
async def shutdown(ctx):
    await ctx.bot.logout()

bot.run(token)
