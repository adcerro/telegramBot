from telegram import Update
import telegram.ext as te
from telegram.ext import MessageHandler, Filters
import logging

#Cruasán icon by Icons8
mytoken = open('token.txt','r').readline()

updater = te.Updater(mytoken)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

helpMessage ='Soy panaBot, un bot capaz de de varias cosas, estos son mis comandos: '

def start(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Saludos!")

def help(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage)

dispatcher.add_handler(te.CommandHandler('start', start))
dispatcher.add_handler(te.CommandHandler(['ayuda','help'], help))
updater.start_polling()