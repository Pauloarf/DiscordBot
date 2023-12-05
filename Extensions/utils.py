import discord
import datetime
from discord.ext import commands 

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='serverinfo',
                brief='Mostra a informação do servidor.',
                help='Com este comando podes ver bastante informação sobre o servidor',
                usage='')
    async def serverinfo(self, ctx : commands.Context):
        bot_m = await ctx.guild.fetch_member(self.bot.user.id)
        guild : discord.Guild = ctx.guild
        n_bots = len([member for member in guild.members if member.bot])
        creation_date : datetime = guild.created_at
        embed = discord.Embed(title=f'{guild.name}')
        embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="Membros",value=guild.member_count)\
            .add_field(name="Humanos",value=f"{guild.member_count - n_bots}")\
            .add_field(name="Bots",value=f"{n_bots}")\
            .add_field(name="Canais de text", value=f"{len([x for x in guild.text_channels if x.permissions_for(bot_m).read_messages])}")\
            .add_field(name="Canais de voz", value=f"{len(guild.voice_channels)}")\
            .add_field(name="Emojis",value=f"{len([x for x in guild.emojis if not x.animated])}/{guild.emoji_limit}",inline=False)\
            .add_field(name="Roles",value=f"{len(guild.roles) - 1}")\
            .add_field(name="Criado a",value=f"{creation_date.year}-{str(creation_date.month).rjust(2,'0')}-{creation_date.day}")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utils(bot))

async def reboot_bot(bot):
    print("Rebooting the bot...")
    await bot.close()
