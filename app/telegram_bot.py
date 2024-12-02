from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(TELEGRAM_BOT_TOKEN)

async def send_message(text, chat_id=CHAT_ID):
    await bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')

