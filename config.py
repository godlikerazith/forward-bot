import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "22383329")
    API_HASH = environ.get("API_HASH", "90012e9940e7c2ce45ccfe7d6bcfe1dd")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7245210989:AAGCtSmRdHzaN6SroGKqiASKBBdrsdZb11k") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ghostcm83:2YpZjH8pafFc9ZJh@cluster0.ohbn7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1918079773').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002423270359'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
