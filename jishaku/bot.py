import discord
from discord.ext import commands
import jishaku
import os


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

token = 'MTE5OTQzMjI4NjQ0NjI5NzI4MA.GBLIqO.GiTbBHLf8lkvHPJwBEhGcQevsPwEcHd04CilLA'

@bot.listen()
async def on_ready():
  print(f"bot ready as {bot.user}")

bot.load_extension('jishaku')
bot.run(token)