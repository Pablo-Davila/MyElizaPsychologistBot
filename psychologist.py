import telebot
import eliza
import sys

therapist = eliza.eliza()
bot = telebot.TeleBot(sys.argv[1])

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
with open("log\log_"+current_time+".txt","w+") as f:
	
	@bot.message_handler(commands=['start', 'help'])
	def send_welcome(message):
		user = message.from_user
		bot.reply_to(message, "Hello " + user.first_name + " " + user.last_name + ".\nHow are you feeling today? Please answer in English.")

	@bot.message_handler(func=lambda message: message.text!="/start")
	def echo_all(message):
		cid = message.chat.id
		
		reply = therapist.respond(message.text)
		bot.send_message(cid, reply)
		
		user = message.from_user
		name = str(user.first_name) + " " + str(user.last_name)
		f.write(name + ": " + message.text + "\n")
		f.write("TO " + name + " " + user.last_name + ": " + reply + "\n")

	print("Running MyElizaPsychologistBot.py")
	bot.polling()