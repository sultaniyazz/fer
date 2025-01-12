import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Dorilarni sotib olish uchun biz bilan bog‘laning. Bizning bot orqali osonlikcha dorilarni tanlab, buyurtma berishingiz mumkin.")

WEBHOOK_URL = "https://fer-rdk8.onrender.com"  

def main():
    app = Application.builder().token(TOKEN).build()

    
    app.add_handler(CommandHandler("start", start))
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
