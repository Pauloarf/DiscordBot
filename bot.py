import asyncio
import os
import discord
import logging
import logging.handlers
from dotenv import load_dotenv
from discord.ext import commands
from help import CustomHelpCommand

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename="Logs/discord.log",
    encoding='utf-8',
    maxBytes= 32*1024*1024,
    backupCount=5
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

intents = discord.Intents(messages=True)
intents.message_content = True
intents.guild_reactions = True
intents.guild_messages = True
intents.guilds = True
intents.dm_messages = True
intents.members = True
    
bot = commands.Bot(
    command_prefix='!',
    case_insensitive=True,
    help_command=CustomHelpCommand(),
    intents=intents
)

async def main():
    for extension in os.listdir("Extensions"):
        if extension[-3:] == '.py':
            try:
                await bot.load_extension(f"Extensions.{extension[:-3]}")
            except Exception as e:
                print(f"Error - Couldn't load extension {extension}\n{e}")
                continue

# Event to print bot information when ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    print(f"The bot is currently in {len(bot.guilds)} guilds.")
    print(f"More info in the Servers_info.log file")
   # for guild in bot.guilds:
    #    if guild.name == "Gunada":
     #       embed = discord.Embed(title='Updates')
      #      embed.set_thumbnail(url=guild.icon.url)
        #    embed.add_field(name="Versão 1.4", value"Comando !serverinfo adicionado")
         #   channel = bot.get_channel(1178677706183946300)  # Replace 'general' with the desired channel name
            #if channel:
                #await channel.send("Estou acordado e pronto para vos mandar à merda")
                #await channel.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    welcome_message = f"MEKIE meu putos, {bot.user.name} na area! Antes de mais muito obrigado por me trazerem para {guild.name}. Avé hitl*r, drogas, techno e LOL!"
    default_channel = guild.text_channels[0] if guild.text_channels else None

    if default_channel and default_channel.permissions_for(guild.me).send_messages:
        await default_channel.send(welcome_message)
    else:
        print(f"Unable to send welcome message to {guild.name}. Check permissions.")

# Event to handle command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Esse comando não existe seu burro. Nem ia dizer nada pq não gosto de ti, mas pronto... Usa !help")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Meu puto... Falta alguma coisa para isso funcionar. Verifica se isso está bem.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Não é suposto colocares isso como argumento. Preciso de te explicar isso como se fosse para mulheres?.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"OUUUU, vamos com calma este comando é como tu, tem delay. Tenta em {error.retry_after:.2f} segundos.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Olha ele... não te armes em campião, se não tens permissão para este comando, então não o usas.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("O pessoal deste server não me deu permissões para fazer isso")
    else:
        # Log the error to console or a log file
        print(f"An error occurred: {type(error).__name__} - {error}")
        # Optionally, send a generic error message to the user
        await ctx.send("Não sei o que se passou, mas não consigo fazer isso... Tou meio burro")

asyncio.run(main())

bot.run(TOKEN, log_handler=None)