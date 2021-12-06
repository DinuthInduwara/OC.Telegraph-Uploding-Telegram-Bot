import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2033518274:AAFYBZRILqiBBDB8_wFaCLSqFQe4mwmGAJs")

    APP_ID = int(os.environ.get("APP_ID", 7122114))

    API_HASH = os.environ.get("API_HASH", "3ff382cb976bdf8aead9359f2c352ac1")
