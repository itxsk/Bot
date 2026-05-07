from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import sys

BOT_TOKEN = os.getenv("8685249061:AAFCFZIbzRoU_yyYPRcsj4ms36H4FZSeJzQ")

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable is missing!")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Bot is running ✅")

if __name__ == "__main__":
    print("🚀 Starting Telegram Bot on Render...")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("✅ Polling started...")
    app.run_polling(drop_pending_updates=True)
