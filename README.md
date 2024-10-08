

# MyElizaPsychologistBot

This Telegram bot implements the famous Eliza psychologist, provided in Python at [eliza.py](https://github.com/jezhiggins/eliza.py) by @jezhiggins.

It is based on [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI"), a Python interface for the [Telegram Bot API](https://core.telegram.org/bots/api).

**Try it in Telegram**: [Psychologist](https://t.me/MyElizaPsychologistBot)


## Usage

To run your own instance of this bot you must first [register a new Telegram bot](https://core.telegram.org/bots#6-botfather). Once you have a token for your bot, you may proceed with options 1 or 2.


### Option 1: Manual execution

First, you have to create an environment variable called "BOT_TOKEN" with the token you obtained in the previous step. After that, you only need the following terminal command:

```Bash
python ./src/psychologist.py
```

This will run the bot attached to your current terminal. If you want it to stay in the background you should have a look at tools like [`tmux`](https://github.com/tmux/tmux).


### Option 2: Docker container (recommended)

First, you have to create a ".env" file in the repository root with the following format:

```
BOT_TOKEN=your_bot_token_here
```

Now, you can run the bot with a single `docker` command:

```Bash
docker compose up -d --build
```

This will run the bot as a Docker container in the background.


## Example

![Conversation example](/img/2020-06-19%20Demo.png "Conversation example")
