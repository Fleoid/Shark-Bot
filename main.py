# bot.py
import os
import random
import discord
import time
from keep_alive import keep_alive

from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


print("starting")

intents = discord.Intents.default()
intents.members = True # Subscribe to the privileged members intent.



bot = commands.Bot(command_prefix='!')

bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    activity = discord.Activity(name='Funny Videos', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


NUMBER = 69


@bot.command(name='rolldice')#, help='Simulates rolling dice.'
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice) )


@bot.command(name='command')#, help='if you put !pop it will say pop.'
async def command(ctx):
    embedVar = discord.Embed(title="Commands", description="Here are a list of commands to use", color=0xed6666)
    embedVar.add_field(name="!rolldice", value="rolls dice ex. !rolldice sides amount", inline=False)
    embedVar.add_field(name="!brrr", value="ex. !brrr @fleoid and\or hi", inline=False)
    await ctx.send(embed=embedVar)


@bot.command(name='numberadd')#, help='if you put !pop it will say pop.'
async def numadd(ctx, num: int):
  global NUMBER
  NUMBER = NUMBER + num
  await ctx.send("The Number is now! " + str(NUMBER))

@bot.command(name='numbersub')#, help='if you put !pop it will say pop.'
async def numsub(ctx, num: int):
  global NUMBER
  NUMBER = NUMBER - num
  await ctx.send("The Number is now! " + str(NUMBER))



@bot.command(name='brrr')#, help='if you put !pop it will say pop.'
async def brrrr(ctx, user: str, text: str):
    if user.find("@") == -1 and text.find("@") == -1:
      await ctx.send("ha ha " + user + "'s " + text + " go brrr")
    else:
      await ctx.send("This Message can't be sent do to it have @ in the message. Sorry \:")


keep_alive()
bot.run(TOKEN)
