import requests
import json
import os
import subprocess
from typing import Dict, Any
import disnake
from disnake import Role
from disnake.ui import Button, View
import json
import os
import time
ENG = {"how setup worker?"}
UKR = {"як встановити воркера?"}
RU = {"как установить воркера?"}
CZ = {}
IT = {}
FR = {}
SP = {}

class greenButton(Button):
    def __init__(self, label: str, bot):
        super().__init__(label=label, style=disnake.ButtonStyle.green)
        self.bot = bot
    async def callback(self, interaction: disnake.Interaction):
        embed = disnake.Embed(
                title="total active worker",
                description="worker",
                color=disnake.Colour.yellow(),
    
            )
        if self.label == "general information":

            
            self.view.clear_items()  
            self.view.add_item(redButton(label="", bot = self.bot))
            self.view.add_item(redButton(label="", bot = self.bot))
            self.view.add_item(redButton(label="", bot = self.bot))
            self.view.add_item(redButton(label="", bot = self.bot))
            pass                
class redButton(Button):
    def __init__(self, label: str, bot, members):
        super().__init__(label=label, style=disnake.ButtonStyle.red)
        self.bot = bot
    async def callback(self, interaction: disnake.Interaction):
        if self.label == "remove imunitet":
            pass




class infoPanel(View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @disnake.ui.button(label="language", style=disnake.ButtonStyle.green, custom_id="admin")
    async def admin(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):


        self.clear_items()  # Очищаємо старі кнопки
        self.add_item(greenButton(label="general information", bot = self.bot))

        await interaction.response.edit_message(content = f"worker panel",view = self)
