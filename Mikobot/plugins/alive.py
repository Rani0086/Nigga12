# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX

# <============================================== IMPORTS =========================================================>
import random
from sys import version_info

import pyrogram
import telegram
import telethon
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Infamous.karma import ALIVE_ANIMATION, ALIVE_BTN
from Mikobot import BOT_NAME, app

# <=======================================================================================================>


# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command("alive"))
async def alive(_, message: Message):
    library_versions = {
        "𝙿𝚃𝙱": telegram.__version__,
        "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽": telethon.__version__,
        "𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼": pyrogram.__version__,
    }

    library_versions_text = "\n".join(
        [f"⌬ **{key}:** `{value}`" for key, value in library_versions.items()]
    )

    caption = f"""**HEY, I AM {BOT_NAME}**

═══════⚡⍟⚡═════════

✪ **𝙲𝚁𝙴𝙰𝚃𝙾𝚁:** [𝙕𝙀𝙉𝙄𝙏𝙎𝙐](https://t.me/about_zenuu)

{library_versions_text}

⌬ **𝙿𝚈𝚃𝙷𝙾𝙽:** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
⌬ **𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:** `2.0`
═════════⚡⍟⚡═════════"""

    await message.reply_animation(
        random.choice(ALIVE_ANIMATION),
        caption=caption,
        reply_markup=InlineKeyboardMarkup(ALIVE_BTN),
    )


# <=======================================================================================================>


# <================================================ NAME =======================================================>
__mod_name__ = "ALIVE"
# <================================================ END =======================================================>
