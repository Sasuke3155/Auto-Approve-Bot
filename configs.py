from os import path, getenv

SUDO = "5171347305"

class Config:
    API_ID = int(getenv("API_ID", "26977508"))
    API_HASH = getenv("API_HASH", "396589629e6705c592bc7fe891dc6e37)
    BOT_TOKEN = getenv("BOT_TOKEN", "7263324595:AAGBFujS3QCBbWyij8JgYhnkZbKuQH12FeM)
    FSUB = getenv("FSUB", "Anime_Aeon")
    CHID = int(getenv("CHID", "-1002011133442"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rishbro:rishbro@cluster0.eiqoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
cfg = Config()
