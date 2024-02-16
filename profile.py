import os
import json
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def getenv(var):
    with open('config.json') as f:
        data = json.load(f)
    return data.get(var)

api_id = int(getenv('API_ID'))
api_hash = getenv('API_HASH')
bot_token = getenv('BOT_TOKEN')

client = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)

def get_dialogs():
    dialogs = []
    last_date = None
    chunk_size = 200
    while True:
        r = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        dialogs.extend(r.dialogs)
        if len(r.dialogs) < chunk_size:
            break
        last_date = dialogs[-1].date
    return dialogs

def main():
    dialogs = get_dialogs()
    for dialog in dialogs:
        print(f"{dialog.name}: {dialog.message}")

if __name__ == '__main__':
    main()
