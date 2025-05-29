from os import path, getenv

class Config:
   CHID = int(getenv("CHID", ""))
    API_HASH = getenv("78d04fae6c5d8416e817ee453c5cac72", "")
    BOT_TOKEN = getenv("7537019943:AAF2N4MG-XQiN7NydSnEGEqN5e3a_wIkTGU", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("1001925074421", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("5841888496", "").split()))
    MONGO_URI = getenv("mongodb+srv://crownexchangeho1:<0aJjVDG5sQxYNFDD>@cluster0.bnp4yk4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
    cfg = Config()

