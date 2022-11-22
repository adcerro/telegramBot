from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton
import telegram.ext as te


list = ['Vivo','Clase','Sexo','Edad','Tiquete','Tarifa','Cabina','Embarque']

buttonsIn = [[InlineKeyboardButton(a,callback_data=list.index(a))] for a in list]

buttons = [[KeyboardButton(a,callback_data=list.index(a))] for a in list]
storage = []
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
    context.bot.send_message(chat_id=update.effective_chat.id,text='Plot bivariable \nSeleccione variable 1:', reply_markup=keys)
    return first

def plotbi2(update: Update, context: te.CallbackContext):
    query = update.callback_query
    storage.append(query.data)
    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable 2:', reply_markup=keys)
    return second
    
def describe(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Seleccione variable:', reply_markup=keys)
    return desc

def cancel(update: Update, context: te.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Cancelado')

def unihandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    print(list[int(query.data)])
    return te.ConversationHandler.END

def deschandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    print(list[int(query.data)])
    return te.ConversationHandler.END
def bihandler(update: Update, context: te.CallbackContext):
    query = update.callback_query
    storage.append(query.data)
    for i in storage:
        print(list[int(i)])
    return te.ConversationHandler.END