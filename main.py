from discord.ext import commands
import os

from scraper import News, Import, Exterminate

bot = commands.Bot(command_prefix='dj ')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


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
    News(thing=[f'{thing}'], count=[f'{count}'])
    titles, links = Import(things=[f'{thing}'])
    Exterminate(things=[f'{thing}'])

    for i, j in zip(titles, links):
        await ctx.send(f"{i} - {j}")

    pass


bot.run(os.getenv('DJ_BOT'))
