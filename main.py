import os
import json
import time
import re
from pyrogram import Client, filters
from pyrogram.types import Message

# Load configuration data from a JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Get environment variables or default values
def getenv(key, default=None):
    return os.environ.get(key, default)

# Initialize the bot client
bot_token = getenv("BOT_TOKEN")
api_hash = getenv("API_HASH")
api_id = getenv("API_ID")

bot = Client("my_bot", api_id, api_hash)

# Function to handle download and upload status
def handle_status(status):
    if status.is_downloading:
        print(f"Downloading: {status.progress}%")
    elif status.is_uploading:
        print(f"Uploading: {status.progress}%")

# Function to handle progress of file transfers
def handle_progress(current, total):
    print(f"Progress: {current}/{total}")

# Function to check if a message contains a valid link
def has_valid_link(message):
    return any(filter(lambda url: url.startswith("https://t.me"), message.text.split()))

# Function to handle start command
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("Welcome! Send me a link to a Telegram post and I will forward it to another chat. Use 'bulk' command to forward multiple posts at once. Supported formats: t.me/xxxx/1001-1010 and t.me/c/xxxx/101-120.")

# Function to handle incoming messages
@bot.on_message(filters.text & filters.private & filters.incoming & filters.user(user_id=bot.me.id) & filters.convert(has_valid_link))
async def forward_post(client, message):
    if "bulk" in message.text.lower():
        # Extract the link from the message
        link = re.findall("https://t.me/.+?/[\d-]+", message.text)[0]

        # Extract the chat ID and message ID from the link
        if "c/" in link:
            chat_id, message_id_range = link.split("c/")[-1].split("/")
            start_message_id = int(message_id_range.split("-")[0])
            end_message_id = int(message_id_range.split("-")[-1])
        else:
            chat_id, message_id = link.split("/")[-2:]
            start_message_id = int(message_id.split("-")[0])
            end_message_id = int(message_id.split("-")[-1])

        # Download the messages
        downloaded_messages = await client.get_messages(chat_id, filter="link", limit=end_message_id - start_message_id + 1, offset=start_message_id)

        # Forward the messages to another chat
        await client.forward_messages("your_chat_id", downloaded_messages)

        # Send a confirmation message
        await message.reply_text(f"{len(downloaded_messages)} messages forwarded successfully!")
    else:
        # Check if the message contains a link to a Telegram post
        if "https://t.me/c/" in message.text:
            # Extract the chat ID and message ID from the link
            chat_id, message_id = message.text.split("/")[-2:]

            # Download the message
            downloaded_message = await client.get_messages(chat_id, message_ids=int(message_id))

            # Forward the message to another chat
            await client.forward_messages("your_chat_id", downloaded_message)

            # Send a confirmation message
            await message.reply_text("Message forwarded successfully!")
        else:
            await
