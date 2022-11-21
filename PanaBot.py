from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove
import telegram.ext as te
import logging
import os
import numpy as np

list = ['Vivo','Clase','Sexo','Edad','Tiquete','Tarifa','Cabina','Embarque']
buttonsIn = [[InlineKeyboardButton(a,callback_data=list.index(a))] for a in list]
buttons = [[KeyboardButton(a,callback_data=list.index(a))] for a in list]
keys = InlineKeyboardMarkup(buttonsIn)
first =0
second =1
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
    options = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,text='Ingrese primera variable',reply_markup=options)
    return first
    
def secondvar(update: Update, context: te.CallbackContext):
    options = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,text='Ingrese segunda variable',reply_markup=options)   
    return second
def okay(update: Update, context: te.CallbackContext):   
    return te.ConversationHandler.END

def describe(update: Update, context: te.CallbackContext):
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

def cancel(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Cancelado')

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
    dispatcher.add_handler(te.ConversationHandler(
    entry_points=[te.CommandHandler('plotbivariate', plotbi)],
    states={
        first: [te.MessageHandler(te.Filters.text,secondvar)],
        second: [te.MessageHandler(te.Filters.text,okay)]
    },fallbacks=[te.CommandHandler('cancelar', cancel)]))
    dispatcher.add_handler(te.CommandHandler('describe', describe))
   
    #updater.idle()
    updater.start_polling()


if __name__ == '__main__':
    main()