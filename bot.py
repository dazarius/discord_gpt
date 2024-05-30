from cog.event.on_msg import on_msg
from command.prefix import command
from command.prefix import SlashCommand
import asyncio
import disnake
from disnake.ext import commands
from disnake.ui import Select, Button
import time
import json
members_db = "members"
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), help_command=None)
@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready.")
#     sql = """
# CREATE TABLE IF NOT EXISTS members (
#     id BIGINT,
#     name VARCHAR(255),
#     warn INT
# )
# """
#     db.cursor.execute(sql)
@bot.event
async def on_member_join(member):
    print("member join!")
    


@bot.command
async def add(ctx, *args, **kwargs):
    for arg in atgs:
        members.append(arg)

bot.add_cog(command(bot))
bot.add_cog(SlashCommand(bot))
members = bot.get_cog('command').get_members()
bot.add_cog(on_msg(bot, members))







bot.run("MTIxNjEwMjE4NDc2MDkwNTkxOA.Gs63P4.7J46EpaHv76aUeqDBUeVUuseHwKyP0G5tvXqpA")
