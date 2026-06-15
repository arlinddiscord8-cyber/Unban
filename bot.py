import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Eingeloggt als {bot.user}")

@bot.tree.command(name="unbanall", description="Entbannt alle gebannten Nutzer")
async def unbanall(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "❌ Du benötigst Administrator-Rechte.",
            ephemeral=True
        )
        return

    await interaction.response.defer()

    bans = [entry async for entry in interaction.guild.bans(limit=None)]

    count = 0
    for ban in bans:
        try:
            await interaction.guild.unban(ban.user)
            count += 1
        except:
            pass

    await interaction.followup.send(
        f"✅ {count} Nutzer wurden entbannt."
    )

bot.run("DEIN_BOT_TOKEN")
