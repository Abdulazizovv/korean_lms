from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHAT_ID = env.int("CHAT_ID")  # Botning chat id raqami
# IP = env.str("ip")  # Xosting ip manzili
# password = env.str("PASSWORD")  # Xosting ip manzili

