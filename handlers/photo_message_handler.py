from telegram import Update
from telegram.ext import ContextTypes

from config import bot_config
from utils.check_admin import get_admin_id

async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admin_id = get_admin_id()

    if update.message.photo:
        photo_file = update.message.photo[-1].file_id
        
        await context.bot.send_photo(chat_id=admin_id, photo=photo_file)
        await update.message.reply_text(bot_config["sended"])