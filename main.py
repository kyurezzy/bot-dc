import os
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot ligado")

@client.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="chat")
    if canal:
        await canal.send(f"👋 Bem-vindo(a), {member.mention}!")

client.run(os.getenv("DISCORD_TOKEN"))
