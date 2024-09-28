from telegram import Update
from telegram.ext import ContextTypes, filters
from config import bot_config
from utils.check_admin import is_admin, get_admin_id

messages = []

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  admin_id = get_admin_id()

  user = update.message.from_user
  text = update.message.text

  if str(user.id) == admin_id:
    messages_count = len(messages)

    if messages_count == 0:
      await update.message.reply_text(bot_config["empty"])
      return

    last_message = messages.pop()
    await update.message.reply_text(f"{bot_config['question']}{last_message}\n\n{bot_config['answer']}>{text}",   parse_mode="MarkdownV2")
  else:
    messages.append(text)
    await update.message.reply_text(bot_config["sended"])
    await context.bot.send_message(chat_id=admin_id, text=f"{bot_config['question']}{text}{bot_config['request_answer']}", parse_mode="MarkdownV2")
