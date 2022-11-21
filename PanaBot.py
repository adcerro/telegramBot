from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import telegram.ext as te
import logging
import os
import numpy as np

list = ['Vivo','Clase','Sexo','Edad','Tiquete','Tarifa','Cabina','Embarque']
buttons = [[InlineKeyboardButton(a,callback_data=list.index(a))] for a in list]
keys = InlineKeyboardMarkup(buttons)

def start(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Saludos {update._effective_message.from_user.first_name}, para ver mis comandos usa /ayuda")

def help(update: Update, context: te.CallbackContext):
    helpMessage = open('helpMessage.txt', 'r').read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage)

def variables(update: Update, context: te.CallbackContext):
    message='Lista de variables: \n'
    for a in list : message= message+ a+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def plotuni(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable:', reply_markup=keys)
    

def plotbi(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable:', reply_markup=keys)

def online():
    mytoken = os.environ["TOKEN"]
    PORT = int(os.environ.get('PORT', '8443'))
    updater = te.Updater(mytoken)
    updater.start_webhook(listen="0.0.0.0",        
                        port=int(PORT),                       
                        url_path=mytoken
                        ,webhook_url='https://panabot-h.herokuapp.com/' + mytoken) 
    return updater

def main():
    #Cruasán icon by Icons8
    mytoken = open('token.txt','r').readline()
    updater = te.Updater(mytoken) 
    #updater = online()

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    dispatcher.add_handler(te.CommandHandler('start', start))
    dispatcher.add_handler(te.CommandHandler(['ayuda','help'], help))
    dispatcher.add_handler(te.CommandHandler('variables', variables))
    dispatcher.add_handler(te.CommandHandler('plotunivariate', plotuni))
    dispatcher.add_handler(te.CommandHandler('plotbivariate', plotbi))
    #updater.idle()
    updater.start_polling()


if __name__ == '__main__':
    main()