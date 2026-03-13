import logging
import os
import telebot
import telebot.types
from dotenv import load_dotenv
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


load_dotenv()
TELEGRAM_BOT_LOG_PATH = os.getenv("TELEGRAM_BOT_LOG_PATH")
if TELEGRAM_BOT_LOG_PATH is None:
    raise ValueError("no log path for the telegram bot in the .env")

os.makedirs(os.path.dirname(TELEGRAM_BOT_LOG_PATH), exist_ok=True)
file_handler = logging.FileHandler(TELEGRAM_BOT_LOG_PATH, mode="a", encoding=None, delay=False)

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s",
                    filename=TELEGRAM_BOT_LOG_PATH,
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if TELEGRAM_BOT_TOKEN is None:
    logger.error("token not foind in the .env")
    raise ValueError("token not found in the .env")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

MINIAPP_URL = os.getenv("MINIAPP_URL")
if MINIAPP_URL is None:
    logger.error("no miniapp url in the .env")
    raise ValueError("no miniapp url in the .env")

@bot.message_handler(commands=["start"])
def start_handler(message: telebot.types.Message):
    miniapp_info = WebAppInfo(url=MINIAPP_URL)

    inline_markup = InlineKeyboardMarkup()
    inline_button = InlineKeyboardButton(
        text="Тык", 
        web_app=miniapp_info
    )
    inline_markup.add(inline_button)

    reply_markup = ReplyKeyboardMarkup()
    reply_button = KeyboardButton(
        text="Тоже тык", 
        web_app=miniapp_info
    )
    reply_markup.add(reply_button)

    bot.send_message(message.chat.id, "Привет, для открытия приложения нажни на кнопку на клавиатуре", reply_markup=reply_markup)
    bot.send_message(message.chat.id, "Или используй кнопку под эти сообщением", reply_markup=inline_markup)

if __name__ == "__main__":
    logger.info("telegram bot started")
    bot.infinity_polling()

