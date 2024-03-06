class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6805772957"
    sudo_users = "6805772957", "851088427"
    GROUP_ID = -1002131909973
    TOKEN = "7030986326:AAHp6WDyj3gkHEQl07XDV1kyrwNppwTcn-E"
    mongo_url = ""
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "W.C_Support"
    UPDATE_CHAT = "W.c_Support"
    BOT_USERNAME = "makewaifucollectionbot"
    CHARA_CHANNEL_ID = "-1002131909973"
    api_id = 23913652
    api_hash = "99383e8046e0d7696aa8d73a504486de"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
