from Extensions.utils import reboot_bot

def handle_console_commands(bot):
    while True:
        command = input("Enter a console command: ")
        if command.lower() == 'reboot':
            reboot_bot(bot)
        elif command.lower() == 'exit':
            print("Exiting console command handler.")
            break
        else:
            print("Invalid command. Available commands: reboot, exit")
