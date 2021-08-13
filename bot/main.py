from datetime import time
from math import e
from asyncio.tasks import wait_for
import discord
from discord import client
from discord.ext import commands
import asyncio
import random
from discord.ext.commands.core import check


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}').format(client)
    
@client.command()
async def fight(ctx, member : discord.Member = None):
    if member is None:
        channelF = ctx.message.channel
        member = ctx.message.author.mention
        await channelF.send(f"Sorry but you can't fight with urself {member}!")
    
    channel = ctx.message.channel
    member1 = ctx.message.author.mention
    member2 = member.mention
    await channel.send(f"**{member1} VS {member2}**")
    await channel.send(f"**{member1} First pick **| punch / defence |**")

    player1 = 100 # Players HP
    player2 = 100 # Second Players HP
    player2_id = client.get_user(member.id) # We need mentioned Players ID

    while True:
        try:
            player_1 = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=20)
        except asyncio.TimeoutError:
            await ctx.send(f"{member1} didn't even attack!")
            break

        if(player_1.content) == "punch":
            dmg = random.randint(1,100)
            player2 = player2 - dmg
            if player2 < 0:
                await ctx.send(f"{member1} ended {member2} with {dmg} dmg.")
                break
            else:
                pass
            await ctx.send(f"{member1} hit a powerful punch {dmg} dmg to {member2} and now he has {player2} HP left.")
            await ctx.send(f"{member2}'s turn pick **| punch / defansgej |**")
        

        if(player_1.content) == "defence":
            armor = random.randint(1,20)
            player1 = player1 + armor
            if player2 < 0:
                await ctx.send(f"{member1} ended {member2} with {dmg} dmg.")
                break
            else:
                pass
            await ctx.send(f"{member1} used 'defence' and got {armor} armor!")
            await ctx.send(f"{member2}'s turn pick **| punch / defence |**")

        try:
           player_2 = await client.wait_for('message', check=lambda message: message.author == player2_id, timeout=20)
        except asyncio.TimeoutError:
            await ctx.send(f"{member2} ran away.")
            break
        if(player_2.content) == "punch":
            dmg2 = random.randint(1,100)
            player1 = player1 - dmg2
            if player1 < 0:
                await ctx.send(f"{member2} ended {member1} with {dmg} dmg.")
                break
            else:
                pass
            await ctx.send(f"{member2} fucking hit a powerful left punch with {dmg2} dmg to {member1} and now he has {player1} HP left.")
            await ctx.send(f"{member1}'s turn pick **| punch / defansgej |**")
        
        if(player_2.content) == "defence":
            armor2 = random.randint(1,20)
            player2 = player2 + armor2
            if player2 < 0:
                await ctx.send(f"{member2} ended {member2} with {dmg} dmg.")
                break
            else:
                pass
            await ctx.send(f"{member2} used 'defansgej' and got {armor2} armor!")
            await ctx.send(f"{member1}'s turn pick **| punch / defansgej |**")

client.run("your token")