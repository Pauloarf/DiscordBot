# DrugAddict Bot (still in development)

## Description

Welcome to @DrugAddict, a Discord bot designed for wild fun and entertainment! This bot is crafted to seamlessly integrate into the unique atmosphere of the specific guild for which it was created. It proudly embraces a distinct personality that includes elements of vulgar vocabulary, references to drugs, dark humor, and more – being as politically incorrect as possible. It's essential to note that all these aspects are intentional and constitute a part of the bot's character. Nothing is meant to be taken seriously or personally.

## Bot Structure

- **botenv**
    - A default and pre-made environment to use the bot straight away.

- **Extensions**
  - `greetings.py`: Handles greeting functionalities.
  - `interactions.py`: Manages various interactive features.
  - `lol_roulette.py`: Implements the LOL roulette command.
  - `nsfw.py`: Manages NSFW content (if applicable).
  - `reactions.py`: Deals with reaction commands.
  - `utils.py`: Provides utility functions.

- **Memes**
  - A directory containing meme images.

- **Nsfw**
  - A directory containing NSFW images.

- **Other Files**
  - `Servers_info.log`: Log file for server information.
  - `discord.log`: Log file with information from the Discord API.
  - `bot.py`: Main script for the bot.
  - `console_commands.py`: Script for console-specific commands.
  - `help.py`: Script handling help-related commands.
  - `toLog.py`: Script for logging functionality.

## Commands (as of 05/12/2023)

- **Greetings**
  - None

- **Lol_roulette**
  - `champ_roll`: Gives a random League of Legends character based on the role.

- **Interact**
  - `quotes`: Get a humorous quote thought up by yours truly.
  - `lol`: Invite someone to play League of Legends.
  - `gay_meter`: Evaluate how "gay" someone is.
  - `quem`: Who?
  - `send_meme`: Display a meme from our database.
  - `store_meme`: Contribute a meme to the database.

- **NSFW**
  - None

- **Utils**
  - `serverinfo`: Display information about the server.

- **Reactions**
  - None

- **Other Commands**
  - `help`: Handles command help messages.

## Disclaimer

DrugAddict Bot boasts a unique personality featuring vulgar vocabulary, drug references, and dark humor, striving to be as politically incorrect as possible. Users interacting with the bot should be aware that these elements are intentional and part of the bot's character. No offense is meant to be taken, and everything is in good humor.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/DrugAddict.git`
2. Install Python dependencies: `pip install -U requirements.txt`
3. Configure your bot token and other settings in `.env`.
4. Run the bot: `python bot.py`

## Usage

- Use the prefix `[!]` to interact with the bot.
- Refer to the documentation for a complete list of commands and features.

## Contributing

The bot is being developed as a side project, purely for fun and learning. Pull requests or suggestions sent to me are appreciated and valued, but there's no certainty that the features would be included!

## License

...

---

**Note:** Always adhere to Discord's terms of service and guidelines when developing and deploying bots on the platform.
