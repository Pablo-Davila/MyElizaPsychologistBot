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

@bot.message_handler(func=lambda message: message.text!="/start")
def echo_all(message):
	'''Answer for each new message.'''
	cid = message.chat.id
	
	reply = therapist.respond(message.text)
	bot.send_message(cid, reply)
	
	user = message.from_user
	name = str(user.first_name) + " " + str(user.last_name)

print("Running MyElizaPsychologistBot.py")
bot.polling()
