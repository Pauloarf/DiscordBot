
servers_file = "Logs/Servers_info.log"
errors_file = "Errors.log"

def store_server_info(bot):
    try:
        with open(servers_file, 'w', encoding='utf-8') as log_file:
            log_file.write(f'The bot is currently in {len(bot.guilds)} guilds.\n')
            
            for guild in bot.guilds:
                log_file.write(f' - {guild}\n')
                log_file.write(f'\tUsers in {guild.name}:\n')
                for member in guild.members:
                    log_file.write(f'\t - {member.name}#{member.discriminator}\n')
    
    except Exception as e:
        print(f'An error occurred: {e}')