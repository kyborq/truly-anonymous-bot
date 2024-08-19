import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start_handler, message_handler

load_dotenv()

def main():
  token = os.getenv("BOT_TOKEN")

  if not token:
    print("Get token from https://t.me/BotFather and set BOT_TOKEN= in .env")
    return
  
  app = ApplicationBuilder().token(token).build()

  app.add_handler(CommandHandler("start", start_handler.start))
  app.add_handler(MessageHandler(filters.TEXT, message_handler.text_message))

  app.run_polling()


if __name__ == '__main__':
  main()