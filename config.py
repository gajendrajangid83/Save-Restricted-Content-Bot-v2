# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25025064"))
API_HASH = getenv("API_HASH", "f9970f147d0bdc333ce0c29c40da4bbb")
BOT_TOKEN = getenv("BOT_TOKEN", "7804036800:AAEFKgbGjX2E11ZWmQtMbzZBJxrSMyYVQD0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "@bosch12345o").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saraswatisharmapbc:L8aRiWhBbhi8mFwN@cluster0.gxhxgye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002825964174"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", "AQF92igAAmdsT0XogB-4njZ-7_3s2tipYFCuN3WMfytQ--OoYLm2VVqnhfkGll0rfp4QWIpMYqCT-OBmLb0DBI0ZGGyJqycwFFNhtiQ9kisNkez5vyJXAkpiOEdxvNuWEgUauPFnwbeWZHEVYNFLfStbCSIEM3rWqturlI5Q0yYTEOtAFag7HyA_CdY3ev9_jKm2n1vlUgI90ru6ySWwVCd7N4BNpYXuZccb4E932cnzXzC8wn1MlTqFF-mRVZkTHNETlMEvXk1LD0SmgWxJBD0klSiBPAjQCtF0rkxanwnfm11pEz3eWT_ods1O31-xEAh15wZ46QFycTcUqfZoaAysWSNhRgAAAAHcmRqkAA")
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
