import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**ʙᴀᴋᴜ ᴀᴢ ᴛᴀɢɢᴇʀ ʙᴏᴛ**\n **ɪʟʀ ɢʀᴜʙᴜɴᴜᴢᴅᴀᴋɪ ʙᴜ̈ᴛᴜ̈ɴ  ɪsᴛɪғᴀᴅᴇᴄ̧ɪʟᴇʀɪ ᴄ̧ᴀɢ̆ɪʀᴀ ʙɪʟᴇʀᴇᴍ \nᴇᴍʀ-ʟᴇʀ ᴜ̈ᴄ̧ᴜ̈ɴ  /melumat ʏᴀᴢ**",
                    buttons=(
                   
		      [Button.url('Mᴇɴɪ ɢʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴇᴛ ➕', f"https://t.me/BakuAzTaggerBot?startgroup=a")],
                      [Button.url('sᴜᴘᴘᴏʀᴛ🔧', f"https://t.me/RowlynUpdateGrub")],
                      [Button.url('Bᴀşǫᴀ ʙᴏᴛʟᴀʀɪᴍɪɴ ᴋᴀɴᴀʟɪ', f"https://t.me/RowlynBots")],
		      [Button.url('Qᴜʀᴀşᴅɪʀɪᴄɪ⚜️', 'https://t.me/Rowlyn')],
                    ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/melumat$"))
async def melumat(event):
  melumattext = "** ʙᴀᴋᴜ ᴀᴢ ᴛᴀɢɢᴇʀ ʙᴏᴛ⚡ ᴇᴍʀʟᴇʀɪ**\n\n**/çağır - ɪsᴛɪғᴀᴅᴇᴄ̧ɪʟᴇʀɪ 5-5 ᴄ̧ᴀɢ̆ɪʀᴀʀ**\n\n**/eçağır - Eᴍᴏᴊɪ ɪʟᴇ ᴄ̧ᴀɢ̆ɪʀᴀʀ**\n\n**/tekliçağır - ɪsᴛɪғᴀᴅᴇᴄ̧ɪʟᴇʀɪ ᴛᴇᴋ-ᴛᴇᴋ ᴄ̧ᴀɢ̆ɪʀᴀʀ**\n\n**/adminçağır - ᴀᴅᴍɪɴʟᴇʀɪ ᴄ̧ᴀɢ̆ɪʀᴀʀ**\n\n**/start - Bᴏᴛᴜ ʙᴀşʟᴀᴅɪʀ**\n \n/vezyet - Bᴏᴛᴜɴ Vᴇᴢʏᴇᴛɪɴɪ Gᴏ̈sᴛᴇʀɪʀ \n\n/hediyye : **Hᴇᴅɪʏʏᴇ ɢᴏ̈ɴᴅᴇʀᴍᴇʏ ɪᴅᴛᴇsᴇɴ ᴛᴏxᴜɴ.** \n \n /reklam - **ʀᴇᴋʟᴀᴍ ᴠᴇ ʏᴀxᴜᴅ ɪş ᴜ̈ᴄ̧ᴜ̈ɴ ʙᴜ ᴇᴍʀ-ɪ ɪşʟᴇᴅɪɴ.**"
  await event.reply(melumattext,
                    buttons=(
                      [Button.url('ᴍᴇɴɪ ɢʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴇᴛ➕', f"https://t.me/BakuAzTaggerBot?startgroup=a")],
                      [Button.url('ᴋᴏ̈ᴍᴇʏ ᴜ̈ᴄ̧ᴜ̈ɴ🔧', f"https://t.me/RowlynUpdateGrub")],
                      [Button.url('Bᴀşǫᴀ ʙᴏᴛʟᴀʀɪᴍɪɴ ᴋᴀɴᴀʟɪ🏆', f"https://t.me/RowlynBots")],
		      [Button.url('ǫᴜʀᴀşᴅɪʀɪᴄɪ⚡', 'https://t.me/Rowlyn')],
                    ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern='^(?i)/saxla'))
async def saxla(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/eçağır ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**ʙᴜ ᴇᴍʀ ᴀɴᴄᴀɢ̆ ɢʀᴜʙ ᴠᴇ ᴋᴀɴᴀʟʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ɪşʟᴇᴅɪʟᴇ ʙɪʟᴇʀ❗** \n@ROWLYN 🍷")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bᴜ ᴇᴍʀ-ɪ ᴀɴᴄᴀɢ̆ ᴀᴅᴍɪɴ/ᴀᴅᴍɪɴᴋᴀʟᴀʀ ɪşʟᴇᴅᴇ ʙɪʟᴇʀ🚬** \n@ROWLYN 🍷")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ᴇᴠᴠᴇʟᴋɪ ᴍᴇsᴀᴊʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ᴛᴀɢ ᴇᴅᴇ ʙɪʟᴍɪʀᴇᴍ**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("ᴄ̧ᴀɢ̆ɪʀᴍᴀɢ̆ Üᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴏxᴅᴜ❗️")
  else:
    return await event.respond("**ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪɴᴇ ʙᴀşʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴀᴢɪɴ...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪ ᴜɢ̆ᴜʀʟᴀ sᴀxʟᴀɴɪʟᴅɪ❌**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪ ᴜɢ̆ᴜʀʟᴀ sᴀxʟᴀɴɪʟᴅɪ\n\n**Bᴜʀᴅᴀ sɪᴢɪɴ ʀᴇᴋʟᴀᴍɪɴɪᴢ ᴏʟᴀ ʙɪʟᴇʀ @ROWLYN**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/saxla'))
async def saxla(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/çağır ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**ʙᴜ ᴇᴍʀ ɢʀᴜʙʟᴀʀ ᴠᴇ ᴋᴀɴᴀʟʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ᴋᴇᴄ̧ᴇʀʟɪᴅɪʀ❗️** \n @ROWLYN 🍷")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**ʙᴜ ᴇᴍʀ ɪ ᴀɴᴄᴀɢ̆ ᴀᴅᴍɪɴʟᴇʀ ɪsᴛɪғᴀᴅᴇ ᴇᴅᴇ ʙɪʟᴇʀ🚬** \n @ROWLYN 🍷")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Eᴠᴠᴇʟᴋɪ ᴍᴇsᴀᴊʟᴀʀᴀ Cᴀᴠᴀʙ Vᴇʀᴍᴇʏɪɴ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("ʙᴀşʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴏxᴅᴜʀ❗️")
  else:
    return await event.respond("ᴄ̧ᴀɢ̆ɪᴛᴍᴀ ᴘʀᴏsᴇsɪɴᴇ  ʙᴀᴄ̧ʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴏxᴅᴜʀ")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"💎 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("ᴘʀᴏsᴇs Uɢ̆ᴜʀʟᴀ Sᴀxʟᴀɴɪʟᴅɪ\n\n**ʙᴜʀᴅᴀ sɪᴢɪɴ ʀᴇᴋʟᴀᴍɪɴᴊᴢ ᴏʟᴀ ʙɪʟᴇʀ @ROWLYN**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"🏆 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("ᴘʀᴏsᴇs ᴜɢ̆ᴜʀʟᴀ ᴅᴀʏᴀɴᴅɪʀɪʟᴅɪ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/saxla'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tekliçağır ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**ʙᴜ ᴇᴍʀ ᴀɴᴄᴀɢ̆ ɢʀᴜʙʟᴀʀ ᴠᴇ ᴋᴀɴᴀʟʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ᴋᴇᴄ̧ᴇʀʟɪᴅɪʀ❗️** \n @ROWLYN 🍷")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bᴜ ᴇᴍʀ ɪ sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴ/ᴀᴅᴍɪɴᴋᴀʟᴀʀ ɪsᴛɪғᴀᴅᴇ ᴇᴅᴇ ʙɪʟᴇʀ🚬**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ᴇᴠᴠᴇʟᴋɪ ᴍᴇsᴀᴊ ᴜ̈ᴄ̧ᴜ̈ɴ ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪ ᴇᴅᴇ ʙɪʟᴍᴇʀᴇᴍ*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("ʙᴀşʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴀᴢɪɴ❗️")
  else:
    return await event.respond("**ᴘʀᴏsᴇsᴇ ʙᴀşʟᴀᴍᴀɢ̆ɪᴍ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴀᴢɪɴ..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**⚡ - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**ᴘʀᴏsᴇs ᴜɢ̆ᴜʀʟᴀ sᴀxʟᴀɴɪʟᴅɪ\n\n**ʙᴜʀᴅᴀ sɪᴢɪɴ ʀᴇᴋşᴀᴍɪɴᴋᴢ ᴏʟᴀ ʙɪʟᴇʀ @ROWLYN**❌****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"💸 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Pʀᴏsᴇs ᴜɢ̆ᴜʀʟᴀ sᴀxʟᴀɴɪʟᴅɪ\n\n**ʙᴜʀᴅᴀ sɪᴢɪɴ ʀᴇᴋʟᴀᴍᴋɴɪᴢ ᴏʟᴀ ʙɪʟᴇʀ @ROWLYN**❌**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/saxla'))
async def saxla(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

sçağır = (
"Bazı insanlar yağmuru hissеdеr, bazıları isе sadеcе ıslanır",
"Unutma; Hеr gеlеn sеvmеz.. Vе hiçbir sеvеn gitmеz",
"Hiç bir canın acısı, sеnin acından az dеğildir",
"Herşeyi denerim; ama yapabildiklerimi yaparım.",
"Aşk bir kadının yaşamının tüm öyküsü, erkeğin ise yalnızca bir serüvenidir.",
"Mutluluk her şeyden önce vücut sağlığındadır.",
"Ne kadar yaşadığımız değil, nasıl yaşadığımız önemlidir",
"Dünya bir gök kuşağı, zihin bir prizma ve varlık ise beyaz bir ışındır.",
"Nereye gittiğini bilmiyorsan, hangi yoldan gittiğinin hiçbir önemi yoktur.",
"Hayatta en değerli olan zamandır. Kime hediye ettiğine dikkat et.",
"Bir evin bütün camlarını kırıp sonra da kapısını çalamazsın.",
"Mutluluk yaşadığın hayat tarzında değil, hayata bakış tarzındadır.",
"Unutma; Hеr gеlеn sеvmеz.. Vе hiçbir sеvеn gitmеz.",
"Yarım nefeslik bu hayatta. Sevgiden başka hiçbir şey planlama...",
"Herkese içindeki iyilik kadar iyi bir hayat dilerim.",
"Güzeli güzel yapan edeptir, edep ise güzeli sevmeye sebeptir!",
"Gül verenin elinde gül kokusu kalır",
"Aradığın seni arayandır.",
"Bir kuş bile nasibi kadar kanat çırpar gökyüzünde.",
"Gönül almayı bilmeyene ömür emanet edilmez",
"Dürüst olmaktan korkma, kaybedeceğin en fazla yanlış insanlar olur.",
"İnsan odun değildir ki, kırıldığı zaman ses çıkarsın.",
"Öğrenmek, yaşamın tek kanıtıdır.",
"Dünya nüfusu arttıkça, insan sayısı azalıyor.",
"Layık olduğunu düşünmediğiniz insanlara asla doğruları söylemeyin.",
"Çok şükür ki gökyüzü henüz hiçbir cüzdana sığmıyor.",
"Kendin ol. Zaten herkes alındı.",
"Canımı yaka yaka, boğazımdaki düğümleri yutkundum.",
"O kadar güzel gülüyordu ki, sevmesem ziyan olacaktı.",
"Sevdiği ben değilim. Size bunun acısını anlatamam.",
"Sevdiği ben değilim. Size bunun acısını anlatamam.",
"Alışıyorsunuz zamanla her şeye ama asla bitmiyor.",
"Eğer doğruyu söylersen hiçbir şeyi hatırlamak zorunda değilsin.",
"Gerçeği ilk sen söyle… Yoksa senin için birisi elbet doğruyu söyleyecektir.",
"Erkekler daha güçlü olabilir ama tahammül eden kadınlardır.",
"Hiçbir acının tarifi yoktur",
"Peşinden gidecek cesaretin varsa, bütün hayaller gerçek olabilir.",
"Gizli aşk bu söyleyemem derdimi hiç kimseye.",
"Aşk her şeyi affeder mi dersin zamanla geçer mi",
"bana bir sigara birde sen lazımsın",
"kimseyi tanımadım ben senden daha özel",
"birgün aşklar biter, hatıralar kalır",
"Sevmek ne uzun kelime!",
"Hatırladığım en unutulası şeysin.",
"Beraber gülmeyi özlediğim insanlar var.",
"Mutluluğu sende bulan senindir ötesi misafir.",
"Zor sev, ama sevmiyorsa zorlama!",
"O kadar güzel gülüyordu ki, sevmesem ziyan olacaktı.",
"ve insan insana yoldaş olmalı yaralarını sarmalı",
"Mezarlık, hırs uğruna pişman olanlarla dolu",
"Aşk rüzgar gibidir, göremezsin ama hissedebilirsin.",
"terazi var tartı var , herşeyin bir vakti var",
"Zihin fukara olunca akıl ukala olurmuş.",
"Yanıltmasın seni masum bakışlar, bazılarını şeytan ayakta alkışlar...",
"hayat yarının bekleyecek kadar uzun değil",
"İyiler asla kaybetmez, kaybedilir.",
"görmezden geldiğin sevgiye muhtaç kalman dileğiyle",
"Keşke akıl vermek yerine huzur verseniz",
"Hiç bilmediğim o kokunu çok özlüyorum",
"İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",
"𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎",
"𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",
"Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧",
"Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛",
"𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛",
"𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",
"𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
"𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",
"𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚",
"𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎",
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",
"İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛",
"Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
"𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",
"𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",
"Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧",
"𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",
"𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
"𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟",
"𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛",
"𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",
"𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı",
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",
"𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟",
"𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
"𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚",
"𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
"İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",
"Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç",
"𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",
"𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚",
"𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟",
"𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢."
)	


@client.on(events.NewMessage(pattern="^/sçağır ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bᴜ ᴇᴍʀ ɢʀᴜʙʟᴀʀ ᴠᴇ ᴋᴀɴᴀʟʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ᴋᴇᴏ̈ᴇʀʟɪᴅɪʀ❗**")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**ʙᴜ ᴇᴍʀ-ɪ ᴀɴᴠᴀɢ̆ ᴀᴅᴍɪɴ/ᴀᴅᴍɪɴᴋᴀʟᴀʀ ɪsᴛɪғᴀᴅᴇ ᴇᴅᴇ ʙɪʟᴇʀ🚬**")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ᴇᴠᴠᴇʟᴋɪ ᴍᴇsᴀᴊʟᴀʀ ᴜ̈ᴄ̧ᴜ̈ɴ ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪɴᴇ ʙᴀşʟᴀʏᴀ ʙɪʟᴍᴇʀᴇᴍ**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("ᴄ̧ᴀɢ̆ɪʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴏxᴅᴜʀ❗️")
  else:
    return await event.respond("**ᴄ̧ᴀɢ̆ɪʀᴍᴀɢ̆ᴀ ʙᴀᴄ̧ʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ sᴇʙᴇʙ ʏᴀᴢɪɴ...!**")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** ᴄ̧ᴀɢ̆ɪʀᴍᴀ ᴘʀᴏsᴇsɪ ᴜɢ̆ᴜʀʟᴀ sᴀxʟᴀɴɪʟᴅɪ❌**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("ᴘʀᴏsᴇs ᴜɢ̆ᴜʀʟᴀ Sᴀxʟᴀɴɪʟᴅɪ\n\n**ʙᴜʀᴅᴀ sɪᴢɪɴ ʀᴇᴋʟᴀᴍɪɴɪᴢ ᴏʟᴀ ʙɪʟᴇʀ @ROWLYNBOTS**❌")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/adminçağır ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)
	
		
@client.on(events.NewMessage(pattern='/alive'))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sᴇɴ ᴍᴇɴɪᴍ sᴀʜɪʙɪᴍ ᴅᴇʏʟsᴇɴ!__")
    await event.reply('**ᴅᴏsᴛᴜᴍ ʙᴏᴛ ɪşʟᴇᴋᴅɪʀ** \n ǫᴜʀᴀşᴅɪʀɪᴄɪ @ROWLYN')

@client.on(events.NewMessage(pattern='/vezyet'))
async def handler(event):
	
    await event.reply('**Tᴀɢɢᴇʀ Bᴏᴛᴜɴ  Vᴇᴢʏᴇᴛ Mᴇɴʏᴜsᴜ** \n Vᴇᴢʏᴇᴛ: ɪşʟᴇᴋᴅɪʀ✅ \n Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪʏᴀsɪ: v1.24.0 \n ᴘʏᴛʜᴏɴ ᴠᴇʀsɪʏᴀsɪ: v3.8+ \n ʙᴏᴛ Vᴇʀsɪʏᴀsɪ: v0.2')

@client.on(events.NewMessage(pattern='/hediyye'))
async def handler(event):
	
    await event.reply('**Tᴀɢɢᴇʀ ʙᴏᴛᴜɴ ʜᴇᴅɪʏʏᴇ ᴍᴇɴʏᴜsᴜ** \n\nLEOʙᴀɴᴋ No: 31 \n\n  🐊')

@client.on(events.NewMessage(pattern='/reklam'))
async def handler(event):
	
    await event.reply('__ʙᴏᴛᴜɴ ʀᴇᴋʟᴀᴍ ᴍᴇɴʏᴜsᴜ__\n**ʀᴇᴋʟᴀᴍ ᴠᴇ ʏᴀxᴜᴅ ɪş ʏᴀxɪɴʟɪɢ̆ɪ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ ** [ʀᴏᴡʟʏɴ](https://t.me/ROWLYN) **ɪʟᴇ sɪᴠʏᴀᴢᴀ Kᴇᴄ̧ɪɴ**')

print(">> Bot işlekdir🚀 @Rowlyn melumat üçün <<")
client.run_until_disconnected()
