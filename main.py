from telegram.ext import Updater, CommandHandler

TOKEN = "توکن_بات_اینجا"

def start(update, context):
    update.message.reply_text("سلام! ربات روشنه ✅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
