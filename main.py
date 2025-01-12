from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram bot tokeningizni kiriting
TOKEN = "7661315158:AAG51v3_qmRTICKWOo3RMw3LjVwutoKz4Y0"

# /start komandasi uchun handler funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Xush kelibsiz!")

# Botni yaratish
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot ishlamoqda...")
    app.run_polling()

if __name__ == "__main__":
    main()
