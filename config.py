import os

# Login feature, if you want then True , if you dont want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is false then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8463456174:AAGr8o9qmwd3EvbObJSbFb0ZJUlFzXvktpo")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28036438"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e77c04deb25085010e82be66d9f5b514")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6201539646"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://bagecob973:Gkbcd3cZ2ejT6Roy@cluster0.uhdadza.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "ROYALBOMMA")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
