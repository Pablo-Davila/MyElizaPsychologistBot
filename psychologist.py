import telebot
import eliza
import sys

therapist = eliza.eliza()
bot = telebot.TeleBot(sys.argv[1])
	
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	'''Welcome message.'''
	user = message.from_user
	bot.reply_to(message, "Hello " + user.first_name + " " + user.last_name + ".\nHow are you feeling today? Please answer me in English.")

@bot.message_handler(func=lambda msg: msg.text[0]!="/")
def echo_all(message):
	'''Answer for each new message.'''
	cid = message.chat.id
	
	reply = therapist.respond(message.text)
	bot.send_message(cid, reply)
	
	user = message.from_user
	name = str(user.first_name) + " " + str(user.last_name)

@bot.message_handler(commands=["git", "github", "source", "src"])
def command_github(message):
	cid = message.chat.id
	
	bot.send_message(cid, "Puedes encontrar el código fuente de este bot en [GitHub](https://github.com/Pablo-Davila/MyElizaPsychologistBot)", parse_mode='Markdown')
	
print("\nRunning MyElizaPsychologistBot.py")
bot.polling()
