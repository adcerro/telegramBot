from telegram import Update
import telegram.ext as te
import logging
import os


def start(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Saludos! {update._effective_message.from_user.first_name}")

def help(update: Update, context: te.CallbackContext):
    helpMessage = open('helpMessage.txt', 'r').read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage)

def main():
    PORT = int(os.environ.get('PORT', 5000))

    #Cruasán icon by Icons8
    #mytoken = open('token.txt','r').readline()
    mytoken = os.environ["TOKEN"]

    updater = te.Updater(mytoken) 

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    updater.start_webhook(listen="0.0.0.0",        
                        port=int(PORT),                       
                        url_path=mytoken) 
    updater.bot.setWebhook('https://panabot-heroku.herokuapp.com/' + mytoken) 
    dispatcher.add_handler(te.CommandHandler('start', start))
    dispatcher.add_handler(te.CommandHandler(['ayuda','help'], help))
    updater.idle()
    #updater.start_polling()


if __name__ == '__main__':
    main()