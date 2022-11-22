from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove
import telegram.ext as te


list = ['Vivo','Clase','Sexo','Edad','Tiquete','Tarifa','Cabina','Embarque']

buttonsIn = [[InlineKeyboardButton(a,callback_data=list.index(a))] for a in list]

buttons = [[KeyboardButton(a,callback_data=list.index(a))] for a in list]

keys = InlineKeyboardMarkup(buttonsIn)

first, second, uni, desc = range(4)
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
    context.bot.send_message(chat_id=update.effective_chat.id,text='Plot univariable \nSeleccione variable:', reply_markup=keys)
    return uni
    
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
    return desc

def cancel(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Cancelado')

def unihandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    match query.data:
        case '0':
            pass
        case '1':
           pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
           pass 
        case '6':
            pass 
        case '7':
            pass
        case '8':
            pass 
    return te.ConversationHandler.END

def deschandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    match query.data:
        case '0':
            pass
        case '1':
           pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
           pass 
        case '6':
            pass 
        case '7':
            pass
        case '8':
            pass 
    return te.ConversationHandler.END