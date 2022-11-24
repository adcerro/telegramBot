from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton
import telegram.ext as te
import Data as da
import os as os

list = ['Sobrevivio','Clase','Sexo','Edad','Hermanos-Pareja','Padres-Hijos','Tarifa','Cabina','Puerto']
glist =['CountPlot','BarPlot','BoxPlot']

buttonsIn = [[InlineKeyboardButton(text=a,callback_data=a)] for a in list]

buttonsInG = [[InlineKeyboardButton(text=b,callback_data=b)] for b in glist]

storage = ['0','0']

keys = InlineKeyboardMarkup(buttonsIn)

keysG = InlineKeyboardMarkup(buttonsInG)

first, second,plot, uni, desc = range(5)
def start(update: Update, context: te.CallbackContext):
    """Sends a greeting message to the user"""

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Saludos {update._effective_message.from_user.first_name}, para ver mis comandos usa /ayuda")

def help(update: Update, context: te.CallbackContext):
    """Shows helpMessage.txt as a message"""

    helpMessage = open('helpMessage.txt', 'r').read()
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage)
    
def variables(update: Update, context: te.CallbackContext):
    """Lists all the variables that can be used, the are stored in list"""

    message='Lista de variables: \n'
    for a in list : message= message+ a+'\n'
    context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def plotuni(update: Update, context: te.CallbackContext):
    """Display intial message after /plotunivariate command

    CommandHandler in the ConversationHandler that initiates the variable selection
    by inlineKeyboard.
    """

    context.bot.send_message(chat_id=update.effective_chat.id,text='Plot univariable \nSeleccione variable:', reply_markup=keys)
    return uni

def plotbi(update: Update, context: te.CallbackContext):
    """Display intial message after /plotbivariate command

    CommandHandler in the ConversationHandler that initiates the variable selection
    by inlineKeyboard.
    """

    context.bot.send_message(chat_id=update.effective_chat.id,text='Plot bivariable \nSeleccione variable 1:', reply_markup=keys)
    return first

def plotbi2(update: Update, context: te.CallbackContext):
    """Prompt for the second variable in the /plotbivariate command

    CallbackQueryHandler in the ConversationHandler recieves the input for the first variable
    and stores it in a list.
    """

    query = update.callback_query
    storage[0]=query.data
    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable 2:', reply_markup=keys)
    return second
    
def describe(update: Update, context: te.CallbackContext):
    """Display intial message after /describe command.

    CommandHandler in the ConversationHandler that initiates the variable selection
    by inlineKeyboard.
    """

    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable:', reply_markup=keys)
    return desc

def cancel(update: Update, context: te.CallbackContext):
    """Stops the command awaiting for an input."""

    context.bot.send_message(chat_id=update.effective_chat.id,text='Cancelado')

def unihandler(update: Update, context: te.CallbackContext):
    """Takes the input of the button in the /plotunivariate command
    
    The input is the callback data of the selected button, which is the index 
    of the variable in the list of variables, then with the data it sends the plots
    of that variable to the user.
    """

    query = update.callback_query
    context.bot.send_message(chat_id=update.effective_chat.id,text='Mostrando gráficas para: '+query.data)
    path =f'uniplots/{query.data.lower()}'
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}2.png','rb'))


    return te.ConversationHandler.END

def deschandler(update: Update, context: te.CallbackContext):
    """Takes the input of the button in the /describe command
    
    The input is the callback data of the selected button, which is the index 
    of the variable in the list of variables.
    """

    query = update.callback_query
    context.bot.send_message(chat_id=update.effective_chat.id,text=f'Información descriptiva de: {query.data}')
    if(query.data in ['Edad','Hermanos-Pareja','Padres-Hijos','Tarifa']):
        context.bot.send_message(chat_id=update.effective_chat.id,text=da.desc(query.data))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text=da.descCat(query.data))
    return te.ConversationHandler.END

def bihandler(update: Update, context: te.CallbackContext):
    """Takes the input of the second button in the /plotbivariate command
    
    The input is the callback data of the selected button, which is the index 
    of the variable in the list of variables. If the same variable was chosen twice
    then an error message is sent by the bot.
    """
    query = update.callback_query
    storage[1]=query.data
    if(storage[0]!=storage[1]):
        context.bot.send_message(chat_id=update.effective_chat.id,text=f'Mostrando gráficas para: {storage[0]} y {storage[1]}')
        try:
            path =f'biplots/{storage[0].lower()}Y{storage[1].lower()}'
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
            try:
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}2.png','rb'))
            except:
                pass
        except:
            path =f'biplots/{storage[1].lower()}Y{storage[0].lower()}'
            try:
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
            except:
                context.bot.send_message(chat_id=update.effective_chat.id,text=f'Lo siento! No tengo gráficas para: {storage[0]} y {storage[1]}')
                #context.bot.send_message(chat_id=update.effective_chat.id,text='Opiciones de gráfico manual:', reply_markup=keysG)
                #return plot
            try: 
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}2.png','rb'))
            except:
                pass

    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text='No se acepta la misma variable dos veces.')
    
    return te.ConversationHandler.END

    

def manualhandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    path =f'biplots/manual{storage[0]}{storage[1]}'
    context.bot.send_message(chat_id=update.effective_chat.id,text='Advertencia, la gráfica es generada por comando en base a su input, por lo que no se puede garantizar al 100 que sea el resultado esperado, o que sea fácil de leer')
    match(query.data):
        case'CountPlot':
            da.countPlot(storage[0],storage[1])
            try:
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
            except:
                context.bot.send_message(chat_id=update.effective_chat.id,text='Lo siento! No pude gráficarlo')
        case'BarPlot':
            da.barPlot(storage[0],storage[1])
            try:
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
            except:
                context.bot.send_message(chat_id=update.effective_chat.id,text='Lo siento! No pude gráficarlo')
        case'BoxPlot':
            da.boxPlot(storage[0],storage[1])
            try:
                context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{path}.png','rb'))
            except:
                context.bot.send_message(chat_id=update.effective_chat.id,text='Lo siento! No pude gráficarlo')
    os.remove(path=f'{path}.png')
    return te.ConversationHandler.END