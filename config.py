import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "26656618")
    API_HASH = environ.get("API_HASH", "2850721c73dbc207b5cf15362c28a66c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7245210989:AAEc1fbBH0RkUv9eqc3Yb2Rzqu7O3wczvpo") 
    BOT_SESSION = environ.get("BOT_SESSION", "RS_Forward_Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://m07490261:razith786@cluster0.lifff.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1918079773').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002423270359'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8001')
    
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
