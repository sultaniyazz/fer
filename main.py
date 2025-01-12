import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Environment Variable orqali TOKEN o'qing
TOKEN = os.getenv("7661315158:AAG51v3_qmRTICKWOo3RMw3LjVwutoKz4Y0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Webhook rejimida ishlayapman!")

# Webhook URL
WEBHOOK_URL = "https://your-bot-url.onrender.com"

def main():
    # Application yarating
    app = Application.builder().token(TOKEN).build()

    # /start komandasi uchun handler qo'shing
    app.add_handler(CommandHandler("start", start))

    # Webhook sozlang
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),  # Render PORT avtomatik sozlanadi
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
