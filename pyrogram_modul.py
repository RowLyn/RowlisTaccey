from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime


app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def _py(client: Client, message: Message):
    await message.reply_text('Pyrogram is a Python library for Telegram bots.')

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''sᴀʟᴀᴍ {msg.from_user.mention} Mᴇɴɪ {msg.chat.title} ɢʀᴜʙᴀ eʟᴀᴠᴇ ᴇᴛᴅɪʏɪɴ ᴜ̈ᴄ̧ᴜ̈ɴ ᴍɪɴɴᴇᴛᴅᴀʀᴀᴍ⚡️\n\nGʀᴜʙᴜɴᴜᴢᴅᴀ 10.000 ᴇ ʏᴀxɪɴ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ ᴄ̧ᴀɢ̆ɪʀᴍᴀǫ ʙᴀᴄᴀʀɪɢ̆ɪᴍ  ᴠᴀʀ ᴇᴍʀ-ʟᴇʀ ᴜ̈ᴄ̧ᴜ̈ɴ /melumat ʏᴀᴢᴍᴀɢ̆ɪᴠɪᴢ ᴋɪғᴀʏᴇᴛᴅɪʀ⚡''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('ɢᴇʟᴇɴ ᴍᴇɴɪᴍ  ǫᴜʀᴀşᴅɪʀɪᴄɪᴍᴅɪʀ.')

 
@app.on_message(filters.command("id"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "User İnfo:\n"
    out_str += f" ⚡️ Gʀᴜʙ ID : {(msg.forward_from_chat or msg.chat).id}\n"
    out_str += f" 💎 ᴄᴀᴠᴀʙʟᴀᴅɪɢ̆ɪɴɪᴢ ɪsᴛɪᴅᴀᴅᴇᴄ̧ɪ Aᴅɪ : {msg.from_user.first_name}\n"
    out_str += f" 💬 Mᴇsᴀᴊ ID : {msg.forward_from_message_id or msg.message_id}\n"
    if msg.from_user:
        out_str += f" 🍷 ᴄᴀᴠᴀʙʟᴀɴᴀɴ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ ID : {msg.from_user.id}\n"
 
    await message.reply(out_str)

@app.on_message(filters.command("melumat"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "User İnfo:\n"
    out_str += f" ⚡️ Gʀᴜʙ ID : {(msg.forward_from_chat or msg.chat).id}\n"
    out_str += f" 💎 Cᴀᴠᴀʙʟᴀɴᴀɴ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ Aᴅɪ : {msg.from_user.first_name}\n"
    out_str += f" 💬 Mᴇsᴀᴊ ID : {msg.forward_from_message_id or msg.message_id}\n"
    if msg.from_user:
        out_str += f" 🍷 Cᴀᴠᴀʙʟᴀɴᴀɴ ɪsᴛɪᴅᴀᴅᴇᴄ̧ɪ ID : {msg.from_user.id}\n"
 
    await message.reply(out_str)

@app.on_message(filters.command("internet"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\nPing: {round(ms)}")
    
app.start()
print(f"Bot pyrogram ( {pyrogram.version} ᴠᴇʀsɪʏᴀsɪ ɪʟᴇ ʙᴀşʟᴀᴅɪʟᴅɪ. ")
idle()
