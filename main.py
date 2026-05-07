from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask
import threading

# ================== Your Simple Bot Code ==================
BOT_TOKEN = os.getenv("BOT_TOKEN")   # ← Must be in Render Environment

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi")

# ================== Flask for Render ==================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is Running ✅"

@flask_app.route('/health')
def health():
    return "OK", 200

def run_bot():
    print("🚀 Starting Telegram Bot (Polling)...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(drop_pending_updates=True)

# ================== Start Everything ==================
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    
    # Start bot in background
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    print(f"🌐 Flask server running on port {PORT}")
    flask_app.run(host="0.0.0.0", port=PORT)
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
