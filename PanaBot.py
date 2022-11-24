import telegram.ext as te
import logging
import os
import Comandos as c

def online():
    """Connects the bot to the webhook in heroku, using the token stored in the app"""
    mytoken = os.environ["TOKEN"]
    PORT = int(os.environ.get('PORT', '8443'))
    updater = te.Updater(mytoken)
    updater.start_webhook(listen="0.0.0.0",        
                        port=int(PORT),                       
                        url_path=mytoken
                        ,webhook_url='https://panabot-h.herokuapp.com/' + mytoken) 
    return updater


first, second,plot, uni, desc = range(5)
def main():
    #Cruasán icon by Icons8
    #mytoken = open('token.txt','r').readline()
    #updater = te.Updater(mytoken) 
    updater = online()

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    dispatcher.add_handler(te.CommandHandler('start', c.start))

    dispatcher.add_handler(te.CommandHandler(['ayuda','help'], c.help))

    dispatcher.add_handler(te.CommandHandler('variables', c.variables))
   
    dispatcher.add_handler(te.ConversationHandler(
    entry_points=[te.CommandHandler('plotbivariate', c.plotbi)],
    states={
        first : [te.CallbackQueryHandler(c.plotbi2)],
        second : [te.CallbackQueryHandler(c.bihandler)],
        plot : [te.CallbackQueryHandler(c.manualhandler)]
    },fallbacks=[te.CommandHandler('cancelar', c.cancel)],allow_reentry=True))

    dispatcher.add_handler(te.ConversationHandler(
    entry_points=[te.CommandHandler('describe', c.describe)],
    states={
        desc : [te.CallbackQueryHandler(c.deschandler)]
    },fallbacks=[te.CommandHandler('cancelar', c.cancel)],allow_reentry=True))

    dispatcher.add_handler(te.ConversationHandler(
    entry_points=[te.CommandHandler('plotunivariate', c.plotuni)],
    states={
        uni: [te.CallbackQueryHandler(c.unihandler)]
    },fallbacks=[te.CommandHandler('cancelar', c.cancel)], allow_reentry=True))
   
    #updater.idle()
    updater.start_polling()


if __name__ == '__main__':
    main()