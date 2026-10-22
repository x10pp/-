import discord
from discord.ext import commands, tasks
from flask import Flask
from threading import Thread

# 1. خادم الويب لإبقاء البوت مستيقظاً 24/7
app = Flask('')

@app.route('/')
def home():
    return "البوت يعمل ويرسل العداد بنجاح!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. إعدادات البوت
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# البيانات الخاصة بك مدمجة وجاهزة
CHANNEL_ID = 1560621843336011779
BOT_TOKEN = "MTU2MjYzOTUwNzY3NTgwNzg3Ng.G7LW0Z.EuTizOFZiU9m0zbmLz1gE6w3Mn-t_lxXIWKIwQ"

@bot.event
async def on_ready():
    print(f'تم تشغيل {bot.user} بنجاح!')
    if not countdown_loop.is_running():
        countdown_loop.start()

# الإرسال تلقائياً كل 5 ساعات
@tasks.loop(hours=5)
async def countdown_loop():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        message_text = (
            "المتبقي <t:1811835600:R>\n"
            "التاريخ <t:1811835600:d>\n"
            "بالتوفيق"
        )
        await channel.send(message_text)

@countdown_loop.before_loop
async def before_countdown():
    await bot.wait_until_ready()

# تشغيل الخادم والبوت
keep_alive()
bot.run(BOT_TOKEN)
