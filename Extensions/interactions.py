import os
import random
import discord
from discord.ext import commands
from datetime import datetime

class Interact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='quotes', brief="Escreve uma quote pensada por mim", help="Este comando imprime uma das varias frases que tenho em mente!")
    async def cp_quotes(self, ctx):
        bot_main_quotes = [
            'Diga sim à cocaína, porque às vezes precisamos de um impulso para fazer coisas que já fazemos, mas com mais velocidade e entusiasmo!',
            ctx.author.display_name + ' o teu pai é Padeiro? É que eu preciso de emprego!'
            'A vida são dois dias, o carnaval são três e o neopop eram 4 :(',
            'Cocaína é a única coisa que te faz sentir invencível até tentares ir às compras e perceberes que voltaste com chamurças.',
            'Eu??? racista?? Nada disso, mas toda a droga é boa... e não vês droga preta pois não?',
            'As mulheres gostam de ser tratadas assim, com chapada na cara, chapada na cona, e soco nas costas! Ass:Paulo Preto',
            'Tou farto de te responder páh! ' + ctx.author.display_name + ', ainda por cima não gosto de ti',
            'Alguém falou em Keta ou alucinei??',
            'LOL is love, LOL is life',
            'Cafeína é minha droga de escolha. Sou tão viciado que meu tipo de sangue agora é A+presso.',
            'Gosto das mulheres como gosto do meu vinho, com alguma idade, numa cave, e trancado.',
            '♪Auf der Heide blüht ein kleines Blümelein♪\n♪Und das heißt♪\n♪Erika♪',
        ]

        response = random.choice(bot_main_quotes)
        await ctx.send(response)

    @commands.command(name='lol', brief="Convida alguem para vir jogar lol")
    async def lol_command(self, ctx, user: discord.User = None):
        await ctx.message.delete()
    
        if user:
            response = f"{user.mention}, OU MENI!!! ANDA LIGA DAS LENDAS COM O {ctx.author.mention}!"
        else:
            response = f"Queres jogar sozinho??? Que cena triste"

        await ctx.send(response)
        
    @commands.command(name='gay_meter', brief="Avalia o quanto gay é uma pessoa")
    async def gay_meter(self, ctx, user: discord.User = None):
        numero = random.randrange(1, 100)

        if user:
            if numero > 20:
                await ctx.send(f"O senhor/a {user.mention} é BUÉ GAY! {numero}% gay na verdade!")
            else:
                await ctx.send(f"O senhor/a {user.mention} é O MAIOR MACHÃO DA ÁREA!  {numero}% gay na verdade!")
        else:
            await ctx.send(f"Olha... não queria dizer nada... mas se não me dás uma pessoa para avaliar assim é dificil")
            
    @commands.command(name='loldle', brief="Site do loldle")
    async def loldle(self, ctx):
        await ctx.send(f"https://loldle.net")
        
    @commands.command(name='quem', brief="quem?")
    async def loldle(self, ctx):
        await ctx.send(f"O CARALHOOOO!")
        
    @commands.command(name='send_meme', brief="Mostrar um meme da nossa database")
    async def send_meme(self, ctx):
        memes_folder = '/home/paulo/Desktop/Projects/DiscordBot/Memes/'
        
        meme_files = [f for f in os.listdir(memes_folder) if os.path.isfile(os.path.join(memes_folder, f))]

    # Check if there are any meme files
        if meme_files:
            image_filename = random.choice(meme_files)

            image_path = os.path.join(memes_folder, image_filename)

            await ctx.send(file=discord.File(image_path, f'{image_filename}'))
        else:
            await ctx.send("OUUU, Não tenho nenhum meme na memória... Manda-me alguns com o !store_meme!")
        
    @commands.command(name='store_meme', brief="Envia um meme para a database")
    async def store_meme(self, ctx):
        if len(ctx.message.attachments) > 0:
            attachment = ctx.message.attachments[0]

            # Save the attachment to a local file
            local_path = f'/home/paulo/Desktop/Projects/DiscordBot/Memes/{attachment.filename}'
            await attachment.save(local_path)

            # Send a confirmation message
            await ctx.send(f"Image saved: .../Memes/")
        else:
            await ctx.send(f"Manda um meme OSTIAAA, vou guardar o quê assim?")
            
            
async def setup(bot):
    await bot.add_cog(Interact(bot))