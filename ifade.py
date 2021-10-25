import os
import discord
import datetime as dt
from discord.ext import commands
from decouple import event
from discord import channel
from dotenv import load_dotenv

PRIMARY_GUILD = " "
PRIMARY_GUILD_KEY = 823567841297327808
WAGON_STEAL_CHANNEL_KEY = 823567841297327742
client = discord.Client()
bot_user = client.user
bot = commands.Bot(command_prefix='!') #özel prefix


#güvenlik önlemi
load_dotenv()
token = os.getenv('token')  # token girin



@client.event
async def on_ready():
    """ Botun hedeflediğimiz sunucuya başarıyla bağlandığını onaylar """
    for guild in client.guilds:
        if guild.name == PRIMARY_GUILD:
            print("Kilitlendi 😎") 
        else:
            print("İsimler uyuşmadı 🤔")

    print(f'{client.user}, {guild.name}'ye başarıyla bağlandı 😁')


@bot.command()
async def phrase(ctx, days: int = None):
    if days:
        after_date = dt.datetime.utcnow()-dt.timedelta(days=days)
       # limit Yok olarak değiştirilebilir, ancak bu onu yavaş bir işlem yapar.
        messages = await ctx.channel.history(limit=10, oldest_first=True, after=after_date).flatten()
        print(messages)
    else:
        await ctx.send("lütfen istediğiniz gün sayısını girin")
