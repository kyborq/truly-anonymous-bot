from telegram import Update
from telegram.ext import ContextTypes
from config import bot_config


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(bot_config["welcome"])
