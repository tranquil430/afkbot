import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio


intents = discord.Intents.default()
intents.members = True
 

client = commands.Bot(command_prefix = '%', intents=intents)

@client.event
async def on_ready():
    print("the bot is ready")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello World")
   
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(523877287716847616)
    await channel.send("Welcome to AFK") 
    cfdncjhbjvksjvds
@client.event
async def on_member_remove(member):
    channel = client.get_channel(523877287716847616)
    await channel.send("Goodbye") 

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source =  FFmpegPCMAudio('E.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You are not in a voice channel")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel") 


client.run(os.environ['TOKEN'])