import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6509707879:AAFk2ztV1nWzQStBTaVCylcAJ_KzCQWL_aA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23214543"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c000fdc4e8f7f9f3b9bb4edd53447b13")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001941131014"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2107223104"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rebon9034:vVVfQDIOnByhXoic@cluster0.twms1nz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001886066580"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝑯𝒆𝒍𝒍𝒐 {first}\n\n𝑰 𝒄𝒂𝒏 𝒔𝒕𝒐𝒓𝒆 𝒑𝒓𝒊𝒗𝒂𝒕𝒆 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝑺𝒑𝒆𝒄𝒊𝒇𝒊𝒆𝒅 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒂𝒏𝒅 𝒐𝒕𝒉𝒆𝒓 𝒖𝒔𝒆𝒓𝒔 𝒄𝒂𝒏 𝒂𝒄𝒄𝒆𝒔𝒔 𝒊𝒕 𝒇𝒓𝒐𝒎 𝒔𝒑𝒆𝒄𝒊𝒂𝒍 𝒍𝒊𝒏𝒌.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1231933846 6566512004 2107223104 1549831164").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.🚫")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝑯𝒆𝒍𝒍𝒐 {𝒇𝒊𝒓𝒔𝒕}\n\n𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒊𝒏 𝒎𝒚 𝑪𝒉𝒂𝒏𝒏𝒆𝒍/𝑮𝒓𝒐𝒖𝒑 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆\n\n𝑲𝒊𝒏𝒅𝒍𝒚 𝑷𝒍𝒆𝒂𝒔𝒆 𝒋𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot of @forwardtarbot If you want this type contact me!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
