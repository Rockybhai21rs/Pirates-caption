import os
import logging
from flask import Flask
from pyrogram import Client, filters
from threading import Thread

# Load environment variables
API_ID = int(os.getenv("API_ID", "12345"))  # Replace with your actual API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Initialize Telegram bot
app = Client("auto_caption_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
flask_app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@flask_app.route('/')
def home():
    return "Bot is running!"

@app.on_message(filters.video | filters.document)
async def auto_caption(client, message):
    new_caption = "Your custom caption here!"  # Customize this logic
    await message.edit_caption(new_caption)

def run_flask():
    flask_app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    app.run()
