from telegram import Update
import telegram.ext as te
import logging
import os


def start(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Saludos {update._effective_message.from_user.first_name}, para ver mis comandos usa /help")

def help(update: Update, context: te.CallbackContext):
    helpMessage = open('helpMessage.txt', 'r').read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage)

def variables(update: Update, context: te.CallbackContext):
    message='Lista de variables: \n'
    list = ['vivo','clase','sexo','edad','tiquete','costo']
    for a in list : message= message+ a+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def online(mytoken):
    mytoken = os.environ["TOKEN"]
    PORT = int(os.environ.get('PORT', '8443'))
    te.Updater(mytoken).start_webhook(listen="0.0.0.0",        
                        port=int(PORT),                       
                        url_path=mytoken
                        ,webhook_url='https://panabot-h.herokuapp.com/' + mytoken) 

def main():
    #Cruasán icon by Icons8
    #mytoken = open('token.txt','r').readline()
    mytoken=''
    online(mytoken)
    

    updater = te.Updater(mytoken) 

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    dispatcher.add_handler(te.CommandHandler('start', start))
    dispatcher.add_handler(te.CommandHandler(['ayuda','help'], help))
    dispatcher.add_handler(te.CommandHandler('variables', variables))
    updater.idle()
    #updater.start_polling()


if __name__ == '__main__':
    main()