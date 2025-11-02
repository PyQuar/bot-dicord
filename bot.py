import discord
from discord.ext import commands

# Create bot with intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def cha9a9a(ctx):
    await ctx.send("BOHMID YA CHA9A9A LALALALA")


@bot.event
async def on_ready():
    print("BOHMID YA CHA9A9A LALALALA")

# When someone joins the server
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")  # You can change this
    if channel:
        await channel.send("#BOYCOTTBOHMID")

# When someone connects (becomes online)
@bot.event
async def on_presence_update(before, after):
    if before.status != after.status and after.status == discord.Status.online:
        channel = discord.utils.get(after.guild.text_channels, name="general")
        if channel:
            await channel.send("#BOYCOTTBOHMID")

bot.run("DISCORD_TOKEN")
