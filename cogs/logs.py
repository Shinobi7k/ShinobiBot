import discord
from discord import app_commands
from discord.ext import commands
import json


#server-log confirm button
class serverConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def server_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != server_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/server_log.json", "r") as f:
            channel = json.load(f)
        with open("jsons/server_log.json", "w") as f:
            channel[str(interaction.user.guild.id)] = server_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Server Log", description = "Your server's updates log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def server_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != server_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#roles confirm button
class rolesConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def roles_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != roles_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/roles_log.json", "r") as f:
            channel = json.load(f)
        with open("jsons/roles_log.json", "w") as f:
            channel[str(interaction.user.guild.id)] = roles_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Roles Log", description = "Your roles' updates log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def roles_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != roles_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#members confirm button
class membersConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def members_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != members_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/members_log.json", "r") as f:
            channel = json.load(f)
        with open("jsons/members_log.json", "w") as f:
            channel[str(interaction.user.guild.id)] = members_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Members Log", description = "Your members' updates log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def members_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != members_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#channels confirm button
class channelsConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def channels_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != channels_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/channels_log.json", "r") as f:
            channel = json.load(f)
        with open("jsons/channels_log.json", "w") as f:
            channel[str(interaction.user.guild.id)] = channels_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Channels Log", description = "Your channels' updates log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def channels_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != channels_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#edits confirm button
class editsConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def edits_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != edits_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/msg_edits.json", "r") as f:
            channel = json.load(f)
        with open("jsons/msg_edits.json", "w") as f:
            channel[str(interaction.user.guild.id)] = edits_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Edited Messages Log", description = "Your edited messages log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def edits_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != edits_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#deletes confirm button
class deletesConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def deletes_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != deletes_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/msg_deletes.json", "r") as f:
            channel = json.load(f)
        with open("jsons/msg_deletes.json", "w") as f:
            channel[str(interaction.user.guild.id)] = deletes_log_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Deleted Messages Log", description = "Your deleted messages log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def deletes_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != deletes_log_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#joins confirm button
class joinsConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def joins_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != joins_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/joins.json", "r") as f:
            channel = json.load(f)
        with open("jsons/joins.json", "w") as f:
            channel[str(interaction.user.guild.id)] = joins_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Joins Log", description = "Your members' joins log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def welcome_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != joins_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#leaves confirm button
class leavesConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def leaves_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != leaves_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/leaves.json", "r") as f:
            channel = json.load(f)
        with open("jsons/leaves.json", "w") as f:
            channel[str(interaction.user.guild.id)] = leaves_channel
            json.dump(channel, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "📝 ┃ Leaved Log", description = "Your members' leaves log channel has been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def welcome_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != leaves_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


class Logs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    #log server command
    @commands.hybrid_command(name = "server-log", with_app_command = True, description = "Log server's updates.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable server's updates log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def server_log(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/server_log.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/server_log.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Server Log", description = "Your server's updates log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Server's updates log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global server_log_author
            global server_log_channel
            server_log_author = ctx.author
            server_log_channel = channel.id
            view = serverConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your server's updates log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @server_log.error
    async def server_log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help server-log` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())


    #log roles command
    @commands.hybrid_command(name = "roles-log", with_app_command = True, description = "Log roles' updates.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable roles' updates log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roles_log(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/roles_log.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/roles_log.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Roles Log", description = "Your roles' updates log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Roles' updates log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global roles_log_author
            global roles_log_channel
            roles_log_author = ctx.author
            roles_log_channel = channel.id
            view = rolesConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your roles' updates log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @roles_log.error
    async def roles_log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help roles-log` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #log members command
    @commands.hybrid_command(name = "members-log", with_app_command = True, description = "Log members' updates.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable members' updates log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def members_log(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/members_log.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/members_log.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Members Log", description = "Your members' updates log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Members' updates log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global members_log_author
            global members_log_channel
            members_log_author = ctx.author
            members_log_channel = channel.id
            view = membersConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your members' updates log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @members_log.error
    async def members_log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help members-log` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #log channels command
    @commands.hybrid_command(name = "channels-log", with_app_command = True, description = "Log channels' updates.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable channels' updates log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def channels_log(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/channels_log.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/channels_log.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Channels Log", description = "Your channels' updates log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Channels' updates log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global channels_log_author
            global channels_log_channel
            channels_log_author = ctx.author
            channels_log_channel = channel.id
            view = channelsConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your channels' updates log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @channels_log.error
    async def channels_log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help channels-log` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #log msg edit command
    @commands.hybrid_command(name = "message-edits", with_app_command = True, description = "Log edited messages and send them to a channel.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable edited messages' log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def msg_edits(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/msg_edits.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/msg_edits.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Edited Messages Log", description = "Your edited messages log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Edited messages' log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global edits_log_author
            global edits_log_channel
            edits_log_author = ctx.author
            edits_log_channel = channel.id
            view = editsConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your edited messages log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @msg_edits.error
    async def msg_edits_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help message-edits` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #log msg delete command
    @commands.hybrid_command(name = "message-deletes", with_app_command = True, description = "Log deleted messages and send them to a channel.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable deleted messages' log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def msg_deletes(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/msg_deletes.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/msg_deletes.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Deleted Messages Log", description = "Your deleted messages log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Deleted messages' log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global deletes_log_author
            global deletes_log_channel
            deletes_log_author = ctx.author
            deletes_log_channel = channel.id
            view = deletesConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your deleted messages log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @msg_deletes.error
    async def msg_deletes_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help message-deletes` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #joins command
    @commands.hybrid_command(name = "joins", with_app_command = True, description = "Log members' joins and send them to a channel.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable members' joins log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def joins(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/joins.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/joins.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Joins Log", description = "Your members' joins log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Members' joins log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global joins_author
            global joins_channel
            joins_author = ctx.author
            joins_channel = channel.id
            view = joinsConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your joins log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @joins.error
    async def joins_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help joins` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #leaves command
    @commands.hybrid_command(name = "leaves", with_app_command = True, description = "Log members' leaves and send them to a channel.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(toggle = "Enable/Disable members' leaves log.", channel = "Channel to send the log.")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def leaves(self, ctx: commands.Context, toggle: app_commands.Choice[str], channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/leaves.json", "r") as f:
                    server_log = json.load(f)
                server_log.pop(str(ctx.guild.id))
                with open("jsons/leaves.json", "w") as f:
                    json.dump(server_log, f, indent=4)
                embed = discord.Embed(title = "📝 ┃ Leaves Log", description = "Your members' leaves log has been disabled succesfully.", color = 0x000000)
                return await ctx.send(embed = embed)
            except:
                return await ctx.send("> Members' leaves log is already disabled in your server.", ephemeral=True)
        if (toggle.value == 'enable'):
            if channel == None:
                return await ctx.send("> You must include a channel to send the log.", ephemeral=True)
            global leaves_author
            global leaves_channel
            leaves_author = ctx.author
            leaves_channel = channel.id
            view = leavesConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {channel.mention} to be your leaves log channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @leaves.error
    async def leaves_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help leaves` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Logs(bot))
