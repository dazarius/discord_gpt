import disnake
from disnake.ext import  commands
from disnake.member import Member
from fabric import Connection
import subprocess
import fabric
import os
import time
import json
import asyncio


def check_user(user_id):
    list_allowed_user = ["912280533155856394", "191164228848189440", "1150908694083686401", "401168753708236820", "1216102184760905918"]
    for user in list_allowed_user:
        if int(user_id) == int(user):
            return True
    return False

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members = []

        """
        Asynchronous function to add members to a list. 

        Args:
            ctx: The context in which the command is being invoked.
            *args: Variable length argument list.

        Returns:
            None
        """
    @commands.command()
    async def add(self, ctx, *args):
        user = disnake.Member
        if check_user(ctx.author.id):
            for arg in args:
                self.members.append(arg)
            await ctx.send(f"{arg} added to list")
        else:
            await ctx.send("You are not allowed to use this command")


        """
        A command that prints the list of members.

        Parameters:
            ctx (Context): The context object representing the invocation context of the command.

        Returns:
            None
        """    
    @commands.command()
    async def l(self, ctx):
        print(f"member list with imunity:{self.members}")

    def get_members(self):
        return self.members
        self.members.clear()

        """
        Executes an SSH key scan for each IP address in the 'server' table of the database.
        This function takes no parameters.

        Returns:
            None
        """
    @commands.command()
    async def fingerprint(self,ctx):
        cursor = db.cursor
        cursor.execute("SELECT ip FROM server")
        rows = cursor.fetchall()
        for row in rows:
            ip = row[0]
            command = f"ssh-keyscan -H {ip} >> ~/.ssh/known_hosts"
            subprocess.run(command, shell=True)
            print(f"Added {ip} to known_hosts")

    @commands.command()
    @commands.is_owner()
    async def addUser(self, ctx):
        if check_user(ctx.author.id):
            db.add_user(ctx.author.id)
            await ctx.send(f"User {ctx.author.name} added.")


        """
        A command that pushes a script to multiple servers.
        """
    @commands.command()
    @commands.is_owner()
    async def push(self, ctx):
        if check_user(ctx.author.id):
            cursor = db.cursor
            cursor.execute("SELECT * FROM server")
            rows = cursor.fetchall()
            count = 0
            failed = 0
            for row in rows:
                ip = row[2]
                command = row[3]
                c = Connection(host=ip, user="root", connect_kwargs={"password": row[4]})
                command = f"echo -e '#!/bin/bash\n\n{command}' > run.sh && chmod +x run.sh"
                try:
                    # c.run("rm run.sh")
                    c.run(f"{command}")
                    print(f"Success with ip: {ip}")
                    count += 1
                except Exception as e:
                    print(f"Failed with ip: {ip}")
                    failed += 1
            await ctx.send(f"Done! Success: {count}\n. Failed: {failed}.") 

    @commands.command()
    @commands.is_owner()
    async def fingerprint(self,ctx):
        if check_user(ctx.author.id):
            cursor = db.cursor
            cursor.execute("SELECT ip FROM server")
            rows = cursor.fetchall()
            
            for row in rows:
                ip = row[0]
                command = f"ssh-keyscan -H {ip} >> ~/.ssh/known_hosts"
                subprocess.run(command, shell=True)
                print(f"Added {ip} to known_hosts")
            await ctx.send("pushed!")



    """
    Runs a script on all servers in the database.

    Parameters:
        ctx (Context): The context object representing the invocation context.

    Returns:
        None
    @commands.command()
    @commands.is_owner()
    async def run(self, ctx):                
        cursor = db.cursor
        ide = ctx.author.id
        cursor.execute("SELECT * FROM server")
        fetch = cursor.fetchall()
        count = 0
        failed = 0
        await ctx.send("running script... it may take a few minutes, during which time the bot will be unresponsive")
        for host in fetch:
            ip = host[2]
            c = Connection(host=ip, user="root", connect_kwargs={"password": host[4]})
            try:
                print(f"Start")
                c.run("./run.sh")
                count += 1
                print(f"Success with ip: {ip}")
            except Exception as e:
                failed += 1
        await ctx.send(f"Success run: {count}\n Failed: {failed}.")
    @commands.command()
    @commands.is_owner()
    async def delete(self, ctx):
        cursor = db.cursor
        ide = ctx.author.id
        cursor.execute("SELECT * FROM server WHERE id = %s", (ide,))
        count = 0
        failed = 0
        await ctx.send("Start deleting... it may take a few minutes, during which time the bot will be unresponsive")
        for host in cursor.fetchall():
            ip = host[2]
            pas = host[4]
            c = Connection(host=ip, user="root", connect_kwargs={"password": pas})
            try:
                c.run("rm run.sh")
                count += 1
                print(f"Success with ip: {ip}")
            except Exception as e:
                failed += 1
                print(f"failed {ip}. Error: {e}")
        await ctx.send(f"Success delete run script on: {count}\n. Failed delete: {failed}.")


    @commands.command()
    async def instalation(self, ctx, *args, **kwargs):
        with open("info/instalation.json", "r") as f:
            data = json.load(f)
            key = args[0]  # Предположим, что args[0] равен "key1"
            value = data[key]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                value_str = ", ".join(value)
            else:
                value_str = str(value)
            await ctx.send(f"{value_str}")
    """

    @commands.command()
    async def breaking_news(self, ctx):
        with open("info/breaking_news.json", "r") as f:
            data = json.load(f)
            embed = disnake.Embed(
                title=data["title"],
                description=data["description"],
                url=data["url"],
                color = disnake.Color.red()
            )
            embed.set_author(name=data["author"])
            await ctx.send(embed=embed)
    @commands.command()
    async def roles(self, ctx, *args, **kwargs):
        with open("info/roles.json", "r") as f:
            data = json.load(f)
            key = args[0]  # Предположим, что args[0] равен "key1"
            value = data["tier"][key]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                value_str = ", ".join(value)
            else:
                value_str = str(value)
            await ctx.send(f"information about role {key}: {value_str}")

    @commands.command()
    async def upgrade(self, ctx):
        with open("filter/upsurge.json", "r") as f:
            data = json.load(f)
        for role_id, users in data.items():
            role = disnake.utils.get(ctx.guild.roles, name=role_id)  # Ищем роль по имени
            if role is None:
                pass
            for user_name in users:
                member = ctx.guild.get_member_named(user_name)
                if member is not None:
                    await member.add_roles(role)
                else:
                    pass
        await ctx.send("promotion was successful!")

    @commands.command()
    async def downgrade(self, ctx):
        with open("filter/downgrade.json", "r") as f:
            data = json.load(f)
        for role_id, users in data.items():
            role = disnake.utils.get(ctx.guild.roles, name=role_id)  # Ищем роль по имени
            if role is None:
                pass
            for user_name in users:
                member = ctx.guild.get_member_named(user_name)
                if member is not None:
                    await member.remove_roles(role)
                else:
                    pass
        await ctx.send("done!")
    @commands.command()
    async def drop(self, ctx):
        with open("info/airdrpinformation.txt", "r") as f:
            drop = f.read()
            await ctx.send(f"actual information about airdrop: {drop}")

class SlashCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    @commands.slash_command()
    async def add_role(self, ctx, member: disnake.Member, role: disnake.Role):
        await member.add_roles(role)
        await ctx.respond(f"Added {role} to {member}")
    @commands.slash_command()
    async def remove_role(self, ctx, member: disnake.Member, role: disnake.Role):
        await member.remove_roles(role)
        await ctx.respond(f"Removed {role} from {member}")



if __name__ == "__main__":
    
    push()
