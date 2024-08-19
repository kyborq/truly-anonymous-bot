from telegram import Update
from telegram.ext import ContextTypes, filters
from config import bot_config
from utils.check_admin import is_admin, get_admin_id

latest_messages = []

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  admin_id = get_admin_id()

  user = update.message.from_user
  text = update.message.text
  
  if not is_admin(user.id):
    latest_messages.append(text)
    last_index = len(latest_messages) - 1
    await update.message.reply_text(bot_config["sended"])
    await context.bot.send_message(chat_id=admin_id, text=latest_messages[last_index])
  else:
    last_index = len(latest_messages) - 1
    last_message = latest_messages[last_index]
    latest_messages.pop(last_index)
    await update.message.reply_text(f"{bot_config["question"]}{last_message}\n\n{bot_config["answer"]}>{text}", parse_mode="MarkdownV2")
    