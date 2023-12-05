import discord
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(**options)

    async def send_bot_help(self, mapping):
        embed_color = 0x3498db
        embed = discord.Embed(title="Comandos Disponíveis", description="TUDO LOUCO COM A QUANTIDADE INCRIVEL DE COISAS QUE EU FAÇO, SOU ENORME", color=embed_color)
        embed.set_thumbnail(url=self.context.bot.user.avatar.url)
        
        for cog, commands in mapping.items():
            if cog:
                name = cog.qualified_name
            else:
                name = "Sem categoria"
            
            value = "\u200b"  # Zero-width space to prevent empty field error
            
            for command in commands:
                value += f"`{command.name}` - {command.short_doc or 'Sem descrição'}\n"
            
            embed.add_field(name=name, value=value, inline=False)

        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=f"{cog.qualified_name} Comandos", description="Comandos nesta categoria:")
        
        for command in cog.get_commands():
            embed.add_field(name=command.name, value=command.short_doc or 'Sem descrição', inline=False)
        
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"Comando: {command.name}", description=command.help)
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=f"Grupo do comando: {group.qualified_name}", description=group.help)
        
        for command in group.commands:
            embed.add_field(name=command.name, value=command.short_doc or 'Sem descrição', inline=False)
        
        await self.get_destination().send(embed=embed)
