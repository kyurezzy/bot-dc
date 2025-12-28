import os
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("BOT CONECTADO COM SUCESSO")

client.run(os.getenv("DISCORD_TOKEN"))
