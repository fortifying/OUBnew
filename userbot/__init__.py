# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """
 
import os
import re
 
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil
 
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon.sync import TelegramClient, custom, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sessions import StringSession
from telethon.utils import get_peer_id
load_dotenv("config.env")
 
 
def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [custom.Button.inline(
        "{} {}".format("🔸", x),
        data="ub_modul_{}".format(x))
        for x in helpable_modules]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("⬅️", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("➡️", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
 
 
# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
 
ASYNC_POOL = []
 
if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)
 
if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)
 
# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)
 
if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)
 
# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)
 
# UserBot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)
 
# Logging channel/group ID configuration
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))
 
# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
 
# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
 
# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
 
# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/fortifying/OUBnew.git")
# UPSTREAM_REPO_URL branch, the default is master
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "phoenix")
 
# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
 
# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)
 
# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
 
# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
 
# Telegraph
TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", None)
 
# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
 
# Chrome sürücüsü ve Google Chrome dosyaları
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
 
# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
 
# Anti Spambot
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
 
# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
 
# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
 
# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
 
# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
 
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None
 
# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
 
# Terminal Alias
TERM_ALIAS = os.environ.get("TERM_ALIAS", None)
 
# Genius Lyrics API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)
 
# Quote
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)
 
# Inline bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
 
# Genius Lyrics API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)
CMD_HELP = {}
 
 
# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')
 
binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}
 
for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)
 
# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)
 
 
if os.path.exists("learning-data-root.check"):
    os.remove("learning-data-root.check")
else:
    LOGS.info("No Braincheck file, fetching ...")
 
URL = 'https://akmj.website/learning-data-root.check'
 
with open('learning-data-root.check', 'wb') as load:
    load.write(get(URL).content)
    
 
if os.path.exists("blacklist.check"):
    os.remove("blacklist.check")
else:
    LOGS.info("No Blacklist check file, fetching ...")
 
URL = 'https://akmj.website/blacklist.check'
 
with open('blacklist.check', 'wb') as load:
    load.write(get(URL).content)    
 
 
async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
            )
        quit(1)
 
    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
 
            )
        quit(1)
 
    elif not BOTLOG or not LOGSPAMMER:
        return
 
    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)
 
 
with bot:
    try:
        bot(JoinChannelRequest("@PakarJembut"))
        bot(JoinChannelRequest("@userbotindo"))       
        
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH
        ).start(bot_token=BOT_TOKEN)
 
        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
 
        @tgbot.on(events.NewMessage(pattern='/start'))
        async def handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'`Phoenix userbot by` @exscythe`! (`@{me.username}`) I am here to help you.`')
            else:
                await event.reply(f'`I work for you :)️`')
 
        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@PakarJembut"):
                rev_text = query[::-1]
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.article(
                    f"Please Use Only With .help Command",
                    text="{}\nTotal loaded modules: {}".format(
                        "Phoenix userbot by @exscythe\n\nhttps://github.com/fortifying/OUBnew", len(dugmeler)),
                    buttons=buttons,
                    link_preview=False
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "© Azurrection",
                    text=f"GTFO Suckers",
                    buttons=[],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "© Azurrection",
                    text="""Bump up Phoenix!
You can convert your account to bot and use them. Remember, you can't manage someone else's bot! All installation details are explained from GitHub address below.""",
                    buttons=[
                        [custom.Button.url("Follow Channel", "https://t.me/userbotindocloud"), custom.Button.url(
                            "Build by", "https://t.me/exscythe")],
                        [custom.Button.url(
                            "GitHub", "https://github.com/fortifying/OUBnew")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)
 
        @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        ))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
 
        @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        ))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1,
                    dugmeler,  # pylint:disable=E0602
                    "helpme"
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
 
        @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"ub_modul_(.*)")
        ))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")
 
                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 90:
                    help_string = str(CMD_HELP[modul_name])[
                        :90] + "\n\nRead more... " + modul_name + " "
                else:
                    help_string = str(CMD_HELP[modul_name])
 
                reply_pop_up_alert = help_string if help_string is not None else \
                    "{} No document has been written for module.".format(
                        modul_name)
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    except:
        LOGS.info(
            "Support for inline is disabled on your bot. "
            "To enable it, define a bot token and enable inline mode on your bot. "
            "If you think there is a problem other than this, contact us."
        )
 
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "ERROR: The BOTLOG_CHATID variable entered is not valid. "
            "Please check the value you entered. "
            "Bot is crashed .."
        )
        quit(1)
 
 
# Global Variables
COUNT_MSG = 0
USERS = {}
BRAIN_CHECKER = []
BLACKLIST = []
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
ISAFK = False
AFKREASON = None
ZALG_LIST = {}