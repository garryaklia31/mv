import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7596211523:AAGmVhgzHxjLTTFiELHsVGSCrSvLxreRuac"
    # Telegram API ki ID
    API_ID = 25773625
    # Telegram API ki hash key
    API_HASH = "137dc2742789fc81191a9bf7a25ff922"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '8039075749'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://harbanssidhu860:MEHAKPREET@cluster0.el4zawv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002635530695
    # Authentication log channel ki ID
    AUTH_LOG = -1002635530695
    # Hit log channel ki ID
    HIT_LOG = -1002635530695
    # DRM dump channel ki ID
    DRM_DUMP = -1002635530695
    # Main channel ki ID
    CHANNEL = -1002635530695
    # Channel ka link
    CH_URL = "https://t.me/PAIDFREE4YOU"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/B3_GOD"
    # Thumbnail image ka URL
    THUMB_URL = "https://graph.org/file/d567886df4483a85e242c-604bb9a48d3d4cf18c.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

