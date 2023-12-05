import random
import asyncio
import discord
from discord.ext import commands

class Lol_rollete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='champ_roll', brief='Seleciona um champion aleatório de lol', help='Select a random champion for a given role. Usage: !champ_roll')
    async def champ_roll(self, ctx):
        roles = ['top', 'mid', 'adc', 'support', 'jungle']
        role_emojis = {'top': '🔝', 'mid': '↗️', 'adc': '🎯', 'support': '🛡️', 'jungle': '🌲'}

        message = await ctx.send(f"Escolhe a tua lane para eu escolher o teu champion, confia que eu sei muito:\n" +
                                "".join([f"{role_emojis[role]} {role.capitalize()}\t" for role in roles]))

        for role in roles:
            await message.add_reaction(role_emojis[role])

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in role_emojis.values()

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            selected_role = next(role for role, emoji in role_emojis.items() if emoji == str(reaction.emoji))
        except asyncio.TimeoutError:
            await ctx.send("FDS meni, demoras tanto que nem sei quem é mais batata, o teu pc ou tu...")
            return

        champions = {
            'top': [
                'Zac', 'Akshan', 'Briar',
                'Gragas', 'Graves', 'Kalista',
                'Malzahar', 'Naafiri', 'Shyvana',
                'Skarner', 'Trundle', 'Udyr',
                'Warwick', 'Xin Zhao', 'Aatrox',
                'Akali', 'Camille', 'Cassiopeia',
                'Cho\'Gath', 'Darius', 'Dr. Mundo',
                'Fiora', 'Gangplank', 'Garen',
                'Gnar', 'Gwen', 'Heimerdinger',
                'Illaoi', 'Irelia', 'Jax',
                'Jayce', 'K\'Sante', 'Kayle',
                'Kennen', 'Kled', 'Lilia',
                'Malphite', 'Maokai', 'Mordekaiser',
                'Nasus', 'Olaf', 'Ornn',
                'Phanteon', 'Poppy', 'Quinn',
                'Renekton', 'Rengar', 'Riven',
                'Rumble', 'Ryze', 'Sett',
                'Shen', 'Singed', 'Sion',
                'Swain', 'Sylas', 'Tahm Kench',
                'Teemo', 'Tryndamere', 'Urgot',
                'Vayne', 'Vladimir', 'Volibear',
                'Wukong', 'Yasuo', 'Yone',
                'Yorick'
                ],
            'mid': [
                'Nunu & Willump', 'Lucien', 'Zilean',
                'Garen', 'Kled', 'Brand',
                'Morgana', 'Singed', 'Teemo',
                'Tryndamere', 'Karthus', 'Gragas',
                'Xin Zhao', 'Kog\'Maw', 'Seraphine',
                'Tristana', 'Ziggs', 'Gangplank',
                'Heimerdinger', 'K\'Sante', 'Kayle',
                'Kennen', 'Nasus', 'Quinn',
                'Riven', 'Qiyana', 'Talon',
                'Zed', 'Cho\'Gath', 'Malphite',
                'Pantheon', 'Rumble', 'Sylas',
                'Diana', 'Ekko', 'Taliyah',
                'Ahri', 'Anivia', 'Annie',
                'Aurelion Sol', 'Azir', 'Corki',
                'Fizz', 'Galio', 'Kassadin',
                'Katarina', 'LeBlanc', 'Lissandra',
                'Lux', 'Neeko', 'Orianna',
                'Syndra', 'Twisted Fate', 'Veigar',
                'Vel\'Koz', 'Vex', 'Viktor',
                'Xerath', 'Zoe', 'Akali',
                'Cassiopeia', 'Irelia', 'Jayce',
                'Renekton', 'Ryze', 'Swain',
                'Vladimir', 'yasuo', 'Yone',
                'Akshan', 'Malzahar', 'Naafiri'
                ],
            'adc': [
                'Cassiopeia', 'Tahm Kench', 'Karthus',
                'Heimerdinger', 'Corki', 'Veigar',
                'Akshan', 'Lucian', 'Kog\'Maw',
                'Seraphine', 'Tristana', 'Ziggs',
                'Swain', 'Yasuo', 'Twitch',
                'Aphelios', 'Ashe', 'Caitlyn',
                'Draven', 'Ezreal', 'Jhin',
                'Jynx', 'Kai\'Sa', 'Miss Fortune',
                'Nilah', 'Samira', 'Sivir',
                'Varus', 'Xayah', 'Zeri',
                'Vayne', 'Kalista'
                ],
            'support': [
                'Galio', 'Poppy', 'Shen',
                'Zac', 'Heimerdinger', 'Ziggs',
                'Gragas', 'Teemo', 'Veigar',
                'Anivia', 'Annie', 'Cho\'Gath',
                'LeBlanc', 'Lissandra', 'Neeko',
                'Zoe', 'Ashe', 'Miss Fortune',
                'Twitch', 'Amumu', 'Fiddlesticks',
                'Ivern', 'Nidalee', 'Zilean',
                'Seraphine', 'Brand', 'Morgana',
                'Swain', 'Lux', 'Malphite',
                'Pantheon', 'Vel\'Koz', 'Xerath',
                'Tahm Kench', 'Alistar', 'Bard',
                'Blitzcrank', 'Braum', 'Janna',
                'Karma', 'Leona', 'Lulu',
                'Maokai', 'Milio', 'Nami',
                'Nautilus', 'Pyke', 'Rakan',
                'Rell', 'Senna', 'Renata Glasc',
                'Sett', 'Shaco', 'Sona',
                'Soraka', 'Taric', 'Thresh',
                'Yummi', 'Zyra'
                ],
            'jungle': [
                'Dr. Mundo', 'Olaf', 'Teemo',
                'Cho\'Gath', 'Twitch', 'Brand',
                'Morgana', 'Malphite', 'Pantheon',
                'Rell', 'Singed', 'Tryndamere',
                'Qiyana', 'Rumble', 'Sylas',
                'Talon', 'Zed', 'Gwen',
                'Mordekaiser', 'Poppy', 'Zac',
                'Gragas', 'Amumu', 'Fiddlesticks',
                'Ivern', 'Nidalee', 'Maokai',
                'Shaco', 'Nunu & Willump', 'Karthus',
                'Xin Zhao', 'Diana', 'Ekko',
                'Taliyah', 'Bel\'Veth', 'Briar',
                'Elise', 'Evelynn', 'Graves',
                'Hecarim', 'Jarvan IV', 'Jax',
                'Kayn', 'Kha\'Zix', 'Kindred',
                'Lee Sin', 'Lilia', 'Master Yi',
                'Nocturne', 'Rammus', 'Rek\'Sai',
                'Rengar', 'Sejuani', 'Shyvana',
                'Skarner', 'Trundle', 'Udyr',
                'Vi', 'Viego', 'Volibear',
                'Warwick', 'Wukong'
                ]
        }

        # Select a random champion for the chosen role
        selected_champion = random.choice(champions.get(selected_role))

        await ctx.send(f"Vais jogar com o/a **{selected_champion}**, e não te esqueças que a tua lane é {selected_role}.\nConfia que está GANHOO")

async def setup(bot):
    await bot.add_cog(Lol_rollete(bot))