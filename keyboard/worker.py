import requests
import json
import os
import subprocess
from typing import Dict, Any
# import database as db
import disnake
from disnake import Role
from disnake.ui import Button, View
import json
import os
import time
# 1cd2f0dc-851f-4ad8-b9f3-30b39f8cbd34


def total_worker(access_token):
    info = "https://production.io.systems/v1/io-explorer/network/info"

    response = requests.get(info, headers={
        "Token": f"{access_token}",
    })
    if response.status_code == 200:
        with open("device.json", "a") as f:
            json.dump(response.json(), f, indent = 4)
        return True
    else:
        return response



class greenButton(Button):
    def __init__(self, label: str, bot):
        super().__init__(label=label, style=disnake.ButtonStyle.green)
        self.bot = bot
    async def callback(self, interaction: disnake.Interaction):
        if self.label == "total worker":
            self.view.clear_items()  
            # await interaction.response.edit_message(content = f"pls DM me user id, to grant them immunity")
            # if total_worker():
            #     dat = total_worker(access_token)
            embed = disnake.Embed(
                title="total active worker",
                description="worker",
                color=disnake.Colour.yellow(),
    
            )   
            with open("device.json", "r") as f:
                data = json.load(f)
            for item in data['data']:
                name = item['name']
                active_gpu = item['active_gpu']
                active_cpu = item['active_cpu']
                total_gpu = item['total_gpu']
                total_cpu = item['total_cpu']
                
                value = f"Active GPU: {active_gpu}\nActive CPU: {active_cpu}\nTotal GPU: {total_gpu}\nTotal CPU: {total_cpu}"
                
                embed.add_field(name=name, value=value, inline=False)
            await interaction.response.send_message(embed=embed)                
class redButton(Button):
    def __init__(self, label: str, bot, members):
        super().__init__(label=label, style=disnake.ButtonStyle.red)
        self.bot = bot
    async def callback(self, interaction: disnake.Interaction):
        if self.label == "remove imunitet":
            pass
class worker_panel(View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @disnake.ui.button(label="worker panel", style=disnake.ButtonStyle.green, custom_id="admin")
    async def admin(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):


        self.clear_items()  # Очищаємо старі кнопки
        self.add_item(greenButton(label="total worker", bot = self.bot))

        await interaction.response.edit_message(content = f"worker panel",view = self)
        

if __name__ == "__main__":
    while True:
        time.sleep(5)

        print(worker(access_token))


