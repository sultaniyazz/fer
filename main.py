import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Environment Variable orqali TOKEN ni o'qing
TOKEN = os.getenv("BOT_TOKEN")  # Bu yerda tokenni faqat Environment Variables orqali olish kerak

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Webhook rejimida ishlayapman!")

# Webhook URL (Render URL-ni to'g'ri kiriting)
WEBHOOK_URL = "https://your-bot-url.onrender.com"  # Bu URL Render.com’dagi haqiqiy URL bilan almashtiring

def main():
    # Application yaratish
    app = Application.builder().token(TOKEN).build()

    # /start komandasi uchun handler qo'shish
    app.add_handler(CommandHandler("start", start))

    # Webhook sozlang
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),  # Render PORT avtomatik sozlanadi
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
