import os 
import logging
from pyrogram import Client, filters
from telegraph import *
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image
import shutil


ocdevs_telegraphbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)


@ocdevs_telegraphbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await ocdevs_telegraphbot.send_message(chat_id=message.chat.id,text="""
       <b>Hey There,
I can upload videos or photos to telegraph.
Hit 'How To Use' button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "How To Use This Bot", callback_data="how_to_use"),
                                        InlineKeyboardButton(
                                            "Other Bots", callback_data="other_bots")
                                    ]]
                            ))

@ocdevs_telegraphbot.on_message(filters.command("botz"))
async def botz(client, message):
   if message.chat.type == 'private':
       await ocdevs_telegraphbot.send_message(chat_id=message.chat.id,text="""
       <b>🔥🔥🔥🔥🔥  Hikzzzz  🔥🔥🔥🔥🔥</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Emma Watson Bot", url='https://t.me/Bot_EmmaWatson_bot'),
                                        InlineKeyboardButton(
                                            "Back", callback_data="start")]]
                            ))


@ocdevs_telegraphbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await ocdevs_telegraphbot.send_message(
               chat_id=message.chat.id,
               text="""<b>How To Use Telegraph Bot!


               
𝙅𝙪𝙨𝙩 𝙨𝙚𝙣𝙙 𝙖 𝙥𝙝𝙤𝙩𝙤 𝙤𝙧 𝙫𝙞𝙙𝙚𝙤 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 𝟱𝙢𝙗 𝙛𝙞𝙡𝙚 𝙨𝙞𝙯𝙚, 𝙄'𝙡𝙡 𝙪𝙥𝙡𝙤𝙖𝙙 𝙞𝙩 𝙩𝙤 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙥𝙝..

Developer :~  ✍️✍️𝓞𝓹𝓮𝓷 𝓒𝓸𝓭𝓮 𝓓𝓮𝓿𝓼 ✍️✍️


    SUPPORTED_MEDIA_TYPES = 
✨ **SUPPORTED MEDIA TYPES** ✨

1) Image
2) Gifs or Animation
3) Video
4) Video Note
5) Document (Video/Photo/Gif)

Note : Telegraph has a size limit of 5 MB</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start")]]))



@ocdevs_telegraphbot.on_message(filters.photo)
async def telephoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/downloads')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@ocdevs_telegraphbot.on_message(filters.animation)
async def teleani_gifs(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/downloads')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Media size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)



@ocdevs_telegraphbot.on_message(filters.document)
async def telephdocs(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/downloads')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Media size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@ocdevs_telegraphbot.on_message(filters.video)
async def televideo(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/downloads')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@ocdevs_telegraphbot.on_message(filters.sticker)
async def getimage(client, message):
#convert To JPG(JPEG)
    """
    im = Image.open('image.jpg').convert('RGB')
    im.save('output.png', 'png')

    """
    dwn = await message.reply_text("Downloading to my server...", True)
    await message.download()
    im = Image.open('downloads/sticker.webp').convert('RGB')
    im.save('downloads/output.jpg', 'jpeg')
    parth = ('downloads/output.jpg')
    await dwn.edit_text("Uploading as telegra.ph link...")
    try:
        url_path = upload_file(parth)[0]
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
    else:
        await dwn.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{url_path}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Open Link", url=f"https://telegra.ph{url_path}"
                    ),
                    InlineKeyboardButton(
                        text="Share Link",
                        url=f"https://telegram.me/share/url?url=https://telegra.ph{url_path}",
                    )
                ]
            ]
        )
    )
    os.remove(parth)
    shutil.rmtree('downloads')

         
         
         
         
@ocdevs_telegraphbot.on_message(filters.video_note)
async def televideonote(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/downloads')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n✍️OpenCode.Devs **',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@ocdevs_telegraphbot.on_callback_query()
async def button(bot, update):
    if "start" in update.data:
        await start(bot, update.message)
        await update.message.delete()
    if "how_to_use" in update.data:
        await help(bot, update.message)
        await update.message.delete()
    if "other_bots" in update.data:
        await botz(bot, update.message)
        await update.message.delete()


print(
    """
Bot Started!
✍️ DᕮᐯᕮᒪOᑭᕮR : OC.Devs
"""
)
ocdevs_telegraphbot.run()
