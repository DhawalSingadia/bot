import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define the API token for your bot
TOKEN = '5701844225:AAFU1aZW4yvuiPbFlLu2IaNcDXdXXKxmWK8'

# Create an instance of the Updater
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher


# Define a handler for copying messages from the channel
def copy_message(update: Update, context):
    message = update.message  # Get the received message
    copied_message = message.text  # Copy the message text
    if len(copied_message) <= 8:
        # Perform actions with the copied message (e.g., save to a database, send it to another chat)
        print("Copied message:", copied_message)


# Register the handler
dispatcher.add_handler(MessageHandler(Filters.text & Filters.chat_type.channel, copy_message))


# Start the bot
updater.start_polling()
updater.idle()
