import telebot
import eliza
import sys

therapist = eliza.eliza()
bot = telebot.TeleBot(sys.argv[1])

def isMessageText(object):
    try:
        if object.content_type == "text":
            return True
        else:
            return False
    except:
        print("Warning: Object checked for text mesage is not even message\n", object)
        return False
	
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	'''Welcome message.'''
	user = message.from_user
	bot.reply_to(
        message,
        f"Hi {user.first_name if user.first_name else 'there!'}{' '+user.last_name if user.last_name else ''}.\nHow are you feeling today? Please answer me in English.")

@bot.message_handler(commands=["git", "github", "source", "src"])
def command_github(message):
	cid = message.chat.id
	
	bot.send_message(cid, "You can find the source code of this bot in [GitHub](https://github.com/Pablo-Davila/MyElizaPsychologistBot)", parse_mode='Markdown')

@bot.message_handler(func=lambda msg: isMessageText(msg))
def echo_all(message):
    '''Answer for each new message.'''
    cid = message.chat.id
    if message.text[0]!="/":
        reply = therapist.respond(message.text)
        bot.send_message(cid, reply)
	
print("\nRunning MyElizaPsychologistBot.py")
bot.polling()
