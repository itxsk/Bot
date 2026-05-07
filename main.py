from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import sys
from flask import Flask
import threading
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable is missing!")
    sys.exit(1)

# ============== Flask (for Render port requirement) ==============
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Telegram Bot is running with Polling ✅"

@flask_app.route('/health')
def health():
    return "OK", 200

# ============== Telegram Bot ==============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Bot is alive with polling.")

def run_bot():
    print("🚀 Starting Telegram Bot Polling...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    # Run bot in background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    print(f"🌐 Starting Flask server on port {PORT}...")
    flask_app.run(host="0.0.0.0", port=PORT)
if __name__ == "__main__":
    # Run bot in background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    print(f"🌐 Starting Flask server on port {PORT}...")
    flask_app.run(host="0.0.0.0", port=PORT)
