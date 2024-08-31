import sys

import telebot

import eliza

therapist = eliza.eliza()
bot = telebot.TeleBot(sys.argv[1])


def is_message_text(object):
    try:
        if object.content_type == "text":
            return True
        else:
            return False
    except:
        print("Warning: Object checked for text message is not a message")
        return False


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user = message.from_user
    bot.reply_to(
        message=message,
        text=(
            f"Hi {user.first_name if user.first_name else 'there!'}"
            f"{' '+user.last_name if user.last_name else ''}."
            "\nHow are you feeling today? Please answer me in English."
        ),
    )


@bot.message_handler(commands=["git", "github", "source", "src"])
def command_github(message):
    cid = message.chat.id

    bot.send_message(
        chat_id=cid,
        text=(
            "You can find the source code of this bot in "
            "[GitHub](https://github.com/Pablo-Davila/MyElizaPsychologistBot)"
        ),
        parse_mode='Markdown',
    )


@bot.message_handler(commands=["id"])
def command_id(message):
    cid = message.chat.id
    bot.send_message(cid, f"Your chat id is {cid}")


@bot.message_handler(func=lambda msg: is_message_text(msg))
def echo_all(message):
    '''Answer for each new message.'''

    cid = message.chat.id
    if message.text[0] != "/":
        reply = therapist.respond(message.text)
        bot.send_message(cid, reply)


print("\nRunning MyElizaPsychologistBot.py")
bot.polling()
