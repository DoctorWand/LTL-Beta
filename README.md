# LogTheLogger
LogTheLogger is an Open Source Discord Bot for Logging onto another Discord Server

Currently Work-In-Progress on Version 1.0, road to 2.0
- See [ROADMAP](ROADMAP.md) for more information

## Dev/Support Discord Server
https://discord.gg/mpgbu3M5Yy

> [!TIP]
> If you can't figure something out, feel free to join the discord mentioned above

## How to setup
1. Invite the Bot on both servers
2. Execute on both servers the `/ltl_setup` command and enter your log channels
3. On the main server execute the `/forwarding-server` command and enter the seconds server id
    1. with executing this command you should start seeing the logs from server A on server B

## Running your own instance
1. Fill out the default_config.json
    1. "discordToken" -> Your Discord bot token
    2. "discordServer" -> Your server id
    3. "discordStatusChannel" -> Your status channel (if you don't have one, leave the 0)
2. Start the start.bat file
> [!IMPORTANT]
> The bot is running on [Python 3.13.3](https://www.python.org/downloads/release/python-3133/)
> You also need to run `python -m pip install discord.py` , `python -m pip install pytz` and `python -m pip install requests` once in CMD with Admin