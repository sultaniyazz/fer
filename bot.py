from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Tokeningizni o'zgartiring
TOKEN = 'YOUR_BOT_TOKEN'

# /start komandasi uchun funksiyani yaratamiz
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom, botga xush kelibsiz!')

def main():
    # Updater ob'ekti yaratamiz
    updater = Updater(TOKEN)
    
    # Dispatcher ni olish
    dispatcher = updater.dispatcher
    
    # /start komandasini qo'shish
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Botni ishga tushuramiz
    updater.start_polling()
    
    # Botni to'xtatish uchun
    updater.idle()

if __name__ == '__main__':
    main()
