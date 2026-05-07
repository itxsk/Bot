import os
import threading
import telebot
from flask import Flask

# ==========================================
# 1. Initialize the Dummy Web Server (Flask)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    print("Someone pinged the web server!")
    return "HTTP Ping received. The container is awake."

def run_web_server():
    # Render assigns a dynamic PORT, default to 3000 for local Termux testing
    port = int(os.environ.get('PORT', 3000))
    # host='0.0.0.0' is mathematically required by Render to expose the port to the internet
    app.run(host='0.0.0.0', port=port)


# ==========================================
# 2. Initialize the Telegram Bot (Polling)
# ==========================================
# Replace with your actual BotFather token
TOKEN = '8685249061:AAFCFZIbzRoU_yyYPRcsj4ms36H4FZSeJzQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    username = message.from_user.username or message.from_user.first_name
    
    # Send response confirming RAM execution
    bot.reply_to(message, f"System is awake. Received: \"{message.text}\"")
    print(f"Responded to message from {username}")

def run_bot():
    print("Bot is polling Telegram servers...")
    # infinity_polling prevents the bot from crashing if Telegram's API has a micro-outage
    bot.infinity_polling()


# ==========================================
# 3. The Execution Matrix (Threading)
# ==========================================
if __name__ == '__main__':
    # We spin up the Flask web server in an isolated background thread
    web_thread = threading.Thread(target=run_web_server)
    web_thread.start()
    
    # We run the heavy bot polling loop on the main thread
    run_bot()
