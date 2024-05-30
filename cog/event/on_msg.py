import disnake
from disnake.ext import commands
import json
import sys
import urlextract
import keyboard.admin as adm
from keyboard.worker import worker_panel
from keyboard.information_panel import infoPanel
from ai import AI

def group_imunitet(roleId):
    with open("filter/roleImunitet.json", "r") as f:
        data = json.load(f)
        for role in data["roles"]:
            if int(role) == int(roleId):
                return True
        return False

detect_link = urlextract.URLExtract()
def detect(text):
    part = text.split(" ")
    with open("filter/filetWords.json", "r") as f:
        data = json.load(f)
        for word in data["words"]:
            if word in text:
                return True
        for url in detect_link.find_urls(text):
            if url in text:
                return True
    return False    








class on_msg(commands.Cog):
    def __init__(self, bot, members_list):
        self.bot = bot
        self.members_list = members_list


    @commands.Cog.listener()
    async def on_message(self, message):
            if message.author == self.bot.user:
                return


            api_key = "sk-proj-eDcqhJNZY1Yijs5UIwEWT3BlbkFJDecEcmnhqxOcJigjeuBT"  # замените на ваш ключ API
            ai = AI(ap=api_key)
            response = ai.max(prompt = message.content)
            await message.channel.send(response)
            if message.content.startswith("$sudo"):
                    await message.channel.send("admin panel", view = adm.admin_panel(self.members_list,self.bot))
            if message.content.startswith("$remove"):
                self.members_list.clear()
            if message.content.startswith("?worker"):
                await message.channel.send("worker panel", view = worker_panel(self.bot))
            if message.content.startswith("?info"):
                await message.channel.send("information panel", view = infoPanel(self.bot))