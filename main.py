import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def main():
    # Create an instance of the Updater class and pass your API token
    updater = Updater(token='YOUR_API_TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the '/start' command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
