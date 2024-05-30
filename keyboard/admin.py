from typing import Dict, Any

import disnake
from disnake import Role
from disnake.ui import Button, View
import json
import os







class greenButton(Button):
    def __init__(self, label: str, bot, members):
        super().__init__(label=label, style=disnake.ButtonStyle.green)
        self.bot = bot
        self.members = members
    async def callback(self, interaction: disnake.Interaction):
        if self.label == "add imunitet":
            self.view.clear_items()  
            # await interaction.response.edit_message(content = f"pls DM me user id, to grant them immunity")
            for member in self.members:
                self.view.add_item(disnake.ui.Button(label=member, style=disnake.ButtonStyle.green, custom_id=member))
            await interaction.response.edit_message(content = f"pls DM me user id, to grant them immunity",view = self.view)
class redButton(Button):
    def __init__(self, label: str, bot, members):
        super().__init__(label=label, style=disnake.ButtonStyle.red)
        self.bot = bot
        self.members = members
    async def callback(self, interaction: disnake.Interaction):
        if self.label == "remove imunitet":
            pass
class admin_panel(View):
    def __init__(self, members_list, bot):
        super().__init__()
        self.bot = bot
        self.user = members_list
        
    @disnake.ui.button(label="admin panel", style=disnake.ButtonStyle.green, custom_id="admin")
    async def admin(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):


        self.clear_items()  # Очищаємо старі кнопки
        self.add_item(greenButton(label="add imunitet", bot = self.bot, members= self.user))
        self.add_item(redButton(label="remove imunitet", bot = self.bot, members= self.user))
        await interaction.response.edit_message(content = f"admin panel",view = self)
        

if __name__ == "__main__":
    os.chdir("../comunity")
    print(os.getcwd())