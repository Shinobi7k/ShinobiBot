import discord
from discord import app_commands
from discord.ext import commands
import json
import asyncio


#hide all confirm
class hideallConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def hideall_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for channel in interaction.guild.channels:
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.read_messages = False
            await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f":closed_lock_with_key: ┃ All Channels Hid! ┃ :closed_lock_with_key:", description=f"> {interaction.user.mention} had hid all channels in the server.")
        await interaction.response.send_message(embed=emb)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def hideall_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#show all confirm
class showallConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def showall_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for channel in interaction.guild.channels:
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.read_messages = True
            await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"👁️ ┃ Channels Showed! ┃ 👁️", description=f"> {interaction.user.mention} had unhid all channels in the server.")
        await interaction.response.send_message(embed=emb)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def showall_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#lock all confirm
class lockallConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def lockall_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for channel in interaction.guild.channels:
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"🔒 ┃ All Channels Locked! ┃ 🔒", description=f"{interaction.user.mention} had locked all channels in the server.")
        await interaction.response.send_message(embed=emb)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def lockall_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#unlock all confirm
class unlockallConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def unlockall_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for channel in interaction.guild.channels:
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"🔓 ┃ All Channels Unlocked! ┃ 🔓", description=f"{interaction.user.mention} had unlocked all channels in the server.")
        await interaction.response.send_message(embed=emb)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def unlockall_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#suggest confirm button
class suggestConfirm(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def suggest_confirm(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != suggest_author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/suggest.json", "r", encoding="utf8") as f:
            channels = json.load(f)
        with open("jsons/suggest.json", "w", encoding="utf8") as f:
            channels[str(interaction.user.guild.id)] = {}
            channels[str(interaction.user.guild.id)]["suggch"] = sugg_ch_id
            channels[str(interaction.user.guild.id)]["revch"] = rev_ch_id
            json.dump(channels, f, sort_keys=True, indent=4, ensure_ascii=False)
        embed = discord.Embed(title = "⚙️ ┃ Suggestions System", description = "Your suggestions channels have been updated succesfully!", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
    #cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def suggest_cancel(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)
        await interaction.response.send_message("> Process Canceled.")


#filter toggle buttons
class filterToggle(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Enable",style=discord.ButtonStyle.green)
    async def filter_enable(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/filter.json", "r") as f:
            toggle = json.load(f)
        try:
            if toggle[str(interaction.user.guild.id)] == "enabled":
                return await interaction.response.send_message("> Your filter is already enabled!", ephemeral = True)
        except:
            toggle[str(interaction.user.guild.id)] = "enabled"
            with open("jsons/filter.json", "w") as f:
                json.dump(toggle, f, indent=4)
            embed = discord.Embed(title = "⚙️ ┃ Bad Words Filter", description = "Bad Words Filter is now **Enabled!**", color = 0x000000)
            await interaction.response.send_message(embed = embed)
            for child in self.children:
                child.disabled=True
            await interaction.message.edit(view=self)
    #disable button
    @discord.ui.button(label="Disable", style=discord.ButtonStyle.red)
    async def filter_disable(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user != author:
            return await interaction.response.send_message("> This is not for you!", ephemeral=True)
        with open("jsons/filter.json", "r") as f:
            toggle = json.load(f)
        try:
            if toggle[str(interaction.user.guild.id)] == "disabled":
                return await interaction.response.send_message("> Your filter is already disabled!", ephemeral = True)
        except:
            return await interaction.response.send_message("> Your filter is already disabled!", ephemeral = True)
        with open("jsons/filter.json", "r") as f:
            toggle = json.load(f)
        toggle.pop(str(interaction.user.guild.id))
        with open("jsons/filter.json", "w") as f:
            json.dump(toggle, f, indent=4)
        embed = discord.Embed(title = "⚙️ ┃ Bad Words Filter", description = "Bad Words Filter is now **Disabled!**", color = 0x000000)
        await interaction.response.send_message(embed = embed)
        for child in self.children:
            child.disabled=True
        await interaction.message.edit(view=self)


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    #suggestions command
    @commands.hybrid_command(name = "suggestions", with_app_command = True, description = "Set channels for suggestions.")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(suggestions_channel = "Set a channel that members will sent their suggetions to.", toggle = "Enable/Disable Suggetions System",
                           review_channel = "Set a private channel for admins to review the suggetions. (or make it the same suggestions channel if you want.)")
    @app_commands.choices(toggle=[
        app_commands.Choice(name="enable", value="enable"),
        app_commands.Choice(name="disable", value="disable")])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def suggestions(self, ctx: commands.Context, toggle: app_commands.Choice[str], suggestions_channel: discord.TextChannel = None, review_channel: discord.TextChannel = None):
        if (toggle.value == 'disable'):
            try:
                with open("jsons/suggest.json", "r", encoding="utf8") as f:
                    channels = json.load(f)
                channels.pop(str(ctx.guild.id))
                with open("jsons/suggest.json", "w", encoding="utf8") as f:
                    json.dump(channels, f, sort_keys=True, indent=4, ensure_ascii=False)
                return await ctx.send("> Suggestions System disabled succecfully.", ephemeral=True)
            except:
                return await ctx.send("> Suggestions System is already disabled in your server.")
        if (toggle.value == 'enable'):
            if suggestions_channel == None or review_channel == None:
                return await ctx.send("> You must include a suggestions channel and a review channel.", ephemeral=True)
            global suggest_author
            global sugg_ch_id
            global rev_ch_id
            suggest_author = ctx.author
            sugg_ch_id = suggestions_channel.id
            rev_ch_id = review_channel.id
            view = suggestConfirm()
            em = discord.Embed(title="Confirmation",
            description=f"Are you sure that you want {suggestions_channel.mention} to be your suggestion channel and {review_channel.mention} to be your suggestions' review channel?",
            colour=discord.Colour.dark_theme())
            await ctx.reply(embed=em, view = view)

    @suggestions.error
    async def suggestions_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help suggestions` for more info",
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


    #filter toggle
    @commands.hybrid_command(name = "filtertoggle", aliases=["filter"], with_app_command = True, description = "Enable/Disable swears filter.")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def filtertoggle(self, ctx):
        global author
        author = ctx.author
        try:
            with open("jsons/filter.json", "r", encoding="utf8") as f:
                toggle = json.load(f)
            if toggle[str(ctx.guild.id)] == "enabled":
                des = "Your swears filter toggle is currently enabled.\nDo you wish to **disable** it?"
            else:
                des = "Your swears filter toggle is currently disabled.\nDo you wish to **enable** it?"
        except:
            des = "Your swears filter toggle is currently disabled.\nDo you wish to **enable** it?"
        view = filterToggle()
        em = discord.Embed(title="Swears Filter!", description=des, colour=discord.Colour.dark_theme())
        await ctx.reply(embed=em, view = view)

    @filtertoggle.error
    async def filtertoggle_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Administrator**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #private channel
    @commands.hybrid_command(name = "prvchannel", aliases=["tempchannel"], with_app_command = True, description = "Makes a temprory private channel.")
    @app_commands.describe(time = "Time of the channel before it gets deleted.", channel_name = "Channel's name.")
    @commands.has_permissions(manage_channels= True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def prvchannel(self, ctx, time, *, channel_name):
        guild = ctx.guild
        category = discord.utils.get(ctx.guild.categories)
        overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        guild.me: discord.PermissionOverwrite(read_messages=True)
                    }
        if time:
            get_time = {
            "s": 1, "m": 60, "h": 3600, "d": 86400,
            "w": 604800, "mo": 2592000, "y": 31104000 }
            timer = time
            a = time[-1]
            b = get_time.get(a)
            c = time[:-1]
            try:
                int(c)
            except:
                return await ctx.reply("> Type time and time unit [s,m,h,d,w,mo,y] correctly.", mention_author=False, ephemeral = True)
            try:
                sleep = int(b) * int(c)
            except:
                return await ctx.reply("> Type time and time unit [s,m,h,d,w,mo,y] correctly.", mention_author=False, ephemeral = True)
        channel = await guild.create_text_channel(name = channel_name , overwrites = overwrites , category = category)
        emb = discord.Embed(title="Channel Created! ✅",
                            description=f"> Private Channel **{channel_name}** has been created for **{timer}**",
                            colour=discord.Colour.dark_theme())
        await ctx.send(embed=emb)
        await asyncio.sleep(int(sleep))
        await channel.delete()
        emb = discord.Embed(title="Channel Deleted!",
                            description=f"> Private Channel **{channel_name}** has been deleted after **{timer}**",
                            colour=discord.Colour.dark_theme())
        await ctx.reply(embed=emb)

    @prvchannel.error
    async def prvchannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help prvchannel` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #change prefix
    @commands.hybrid_command(name = "prefix", aliases=["changeprefix"], with_app_command = True, description = "Changes the prefix for a server.")
    @app_commands.describe(prefix = "The new prefix.")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def prefix(self, ctx, prefix):
        with open("jsons/prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("jsons/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        prefix_embed = discord.Embed(title="Prefix Changed!",
        description=f"Prefix has been changed to {prefix}",
        colour=discord.Colour.blue())
        await ctx.send(embed=prefix_embed)

    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Administrator**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.MissingRequiredArgument):
            arg_error = discord.Embed(title="Missing Argument!",
            description=f"> Please check `_help prefix` for more info",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=arg_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #hide
    @commands.hybrid_command(name = "hide", with_app_command = True, description = "Hide a channel.")
    @app_commands.describe(channel = "Channel to hide (default is current channel).")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hidechat(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.read_messages == False:
            await ctx.reply("> The channel is already hidden!", mention_author=False, ephemeral = True)
            return
        overwrite.read_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f":closed_lock_with_key: ┃ Channel Hid!",
                            description=f"> **{channel.mention}** has been hidden.",
                            colour=discord.Colour.dark_theme())
        await ctx.send(embed=emb)

    @hidechat.error
    async def hidechat_error(self, ctx, error):
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


    #hide all
    @commands.hybrid_command(name = "hideall", with_app_command = True, description = "Hide all channels in the server.")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hideall(self, ctx):
        global author
        author = ctx.author
        hideall_em = discord.Embed(title="Confirm", description="Are you sure that you want to hide all your channels?")
        view = hideallConfirm()
        await ctx.send(embed=hideall_em, view=view)

    @hideall.error
    async def hideall_error(self, ctx, error):
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


    #show
    @commands.hybrid_command(name = "show", aliases=["unhide"], with_app_command = True, description = "Show a hidden channel.")
    @app_commands.describe(channel = "Channel to unhide (default is current channel).")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def showchat(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.read_messages == True:
            await ctx.reply("> The channel is already shown!", mention_author=False, ephemeral = True)
            return
        overwrite.read_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"👁️ ┃ Channel Showed!",
                            description=f"> **{channel.mention}** has been shown.",
                            colour=discord.Colour.dark_theme())
        await ctx.send(embed=emb)

    @showchat.error
    async def showchat_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            per_error = discord.Embed(title="Missing Permissions!",
            description=f"> You must have __**Manage Channels**__ permission!",
            colour=discord.Colour.light_grey())
            await ctx.reply(embed=per_error, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            cool_error = discord.Embed(title=f"Slow it down bro!",
            description=f"> Try again in {error.retry_after:.2f}s.",colour=discord.Colour.light_grey())
            await ctx.reply(embed=cool_error, ephemeral=True)


    #show all
    @commands.hybrid_command(name = "showall", with_app_command = True, description = "Unhide all channels in the server.")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def showall(self, ctx):
        global author
        author = ctx.author
        hideall_em = discord.Embed(title="Confirm", description="Are you sure that you want to unhide all your channels?")
        view = showallConfirm()
        await ctx.send(embed=hideall_em, view=view)

    @showall.error
    async def showall_error(self, ctx, error):
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


    #lock
    @commands.hybrid_command(name = "lock", with_app_command = True, description = "Lockes a channel.")
    @app_commands.describe(channel = "Channel to lock (default is current channel).")
    @commands.has_permissions(manage_channels = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def lock(self, ctx: commands.Context, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == False:
            return await ctx.reply("> The channel is already locked", mention_author=False, ephemeral = True)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"🔒 ┃ Channel Locked!",
                            description=f"> **{channel.mention}** has been locked.",
                            colour=discord.Colour.dark_theme())
        await ctx.send(embed=emb)

    @lock.error
    async def lock_error(self, ctx, error):
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


    #lock all
    @commands.hybrid_command(name = "lockall", with_app_command = True, description = "Lockes all the channels.")
    @commands.has_permissions(manage_channels = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def lockall(self, ctx: commands.Context):
        global author
        author = ctx.author
        lockall_em = discord.Embed(title="Confirm", description="Are you sure that you want to lock all your channels?")
        view = lockallConfirm()
        await ctx.send(embed=lockall_em, view=view)

    @lockall.error
    async def lockall_error(self, ctx, error):
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


    #unlock
    @commands.hybrid_command(name = "unlock", with_app_command = True, description = "Unlocks a locked channel.")
    @app_commands.describe(channel = "Channel to unlock (default is current channel).")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unlock(self, ctx: commands.Context, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == True:
            return await ctx.reply("> The channel is already unlocked", mention_author=False, ephemeral = True)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        emb = discord.Embed(title=f"🔓 ┃ Channel Unlocked!",
                            description=f"> **{channel.mention}** has been unlocked.",
                            colour=discord.Colour.dark_theme())
        await ctx.send(embed=emb)

    @unlock.error
    async def unlock_error(self, ctx, error):
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


    #unlock all
    @commands.hybrid_command(name = "unlockall", with_app_command = True, description = "unlockes all the channels.")
    @commands.has_permissions(manage_channels = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unlockall(self, ctx: commands.Context):
        global author
        author = ctx.author
        unlockall_em = discord.Embed(title="Confirm", description="Are you sure that you want to unlock all your channels?")
        view = unlockallConfirm()
        await ctx.send(embed=unlockall_em, view=view)

    @unlockall.error
    async def unlockall_error(self, ctx, error):
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
    await bot.add_cog(Settings(bot))
