from telegram import Update
from telegram.ext import ContextTypes, filters
from config import bot_config
from utils.check_admin import is_admin, get_admin_id

last_messages = []

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  admin_id = get_admin_id()

  user = update.message.from_user
  text = update.message.text

  if not is_admin(user.id):
    last_messages.append(text)
    await update.message.reply_text(bot_config["sended"])
    await context.bot.send_message(chat_id=admin_id, text=f"{bot_config['question']}{text}", parse_mode="MarkdownV2")
  else:
    last_index = len(last_messages) - 1
    last_message = last_messages[last_index]
    await update.message.reply_text(f"{bot_config['question']}{last_message}\n\n{bot_config['answer']}>{text}", parse_mode="MarkdownV2")
