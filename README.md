# Moji

**This is a work in progress, contributions are welcome**

[Invite the bot to your server](https://discordapp.com/oauth2/authorize?client_id=434439958128885760&scope=bot)

Improve your texts to your girlfriend, communicate with your children, spice up your doctoral thesis, Moji gives you something you never thought you needed.

Turn this
> Please give me a passing grade, professor. I'm going to fail out of university if you don't.

To this:fire::fire::fire::
> Please:pray::pray:give me a passing:ticket::ticket:grade, professor.:woman:‍:school:I'm going to fail:poop:out of university:mortar_board::mortar_board::mortar_board:if you don't.

Currently uses a filtered version of [emojilib](https://github.com/muan/emojilib) for emoji keyword mapping.

### Calling the bot

Just mention it and give it your message.

```
@Moji <Your message here>
```

### Running the bot

Moji uses the env var `DISCORD_TOKEN` for its token, so make sure that this is configured.

**Linux/Mac OS**

```
pip install -r requirements.txt
python3 moji_bot.py
```

**Windows**
1. Get linux/windows subsystem for linux
2. Refer to linux instructions

