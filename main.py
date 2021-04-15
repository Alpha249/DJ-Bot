from discord.ext import commands
import discord
from scraper import News

import os


bot = commands.Bot(command_prefix='DJ!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 100, 2)}ms')


@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def news(ctx, thing, count):
    title, link = News(thing=thing, count=count)
    print(title)
    print(link)
    for i in range(int(count)):
        print(title)
        print(list)
        await ctx.send(f"{title[i]} - {link[i]}")
    title.clear()
    link.clear()





bot.run(os.getenv('DJ_BOT'))
