import os
from pyrogram import Client, filters
from pyrogram.types import Message

# 🔑 Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
FORCE_SUB_CHANNEL1 = os.environ.get("FORCE_SUB_CHANNEL1")  # @instagamov
FORCE_SUB_CHANNEL2 = os.environ.get("FORCE_SUB_CHANNEL2")  # @tZvUvt1zp1w0ZDU1

# ✅ Bot Client
app = Client(
    "terabox-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 🔎 Force Subscribe Check
async def force_sub(client, message: Message):
    try:
        user = await client.get_chat_member(FORCE_SUB_CHANNEL1, message.from_user.id)
        user2 = await client.get_chat_member(FORCE_SUB_CHANNEL2, message.from_user.id)
        if (user.status in ["member", "administrator", "creator"]) and (user2.status in ["member", "administrator", "creator"]):
            return True
    except:
        pass
    return False

# 🚀 Start Command
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    if not await force_sub(client, message):
        await message.reply_text(
            f"🚨 Pehle dono channels join karo:\n👉 {FORCE_SUB_CHANNEL1}\n👉 {FORCE_SUB_CHANNEL2}\n\nPhir /start dobara bhejo."
        )
        return
    await message.reply_text("👋 Hello! Mujhe Terabox link bhejo, mai aapko download link ya file bhej dunga.")

# 📥 Terabox Link Handler
@app.on_message(filters.text & ~filters.command("start"))
async def get_file(client, message: Message):
    if not await force_sub(client, message):
        await message.reply_text(
            f"🚨 Pehle dono channels join karo:\n👉 {FORCE_SUB_CHANNEL1}\n👉 {FORCE_SUB_CHANNEL2}\n\nPhir dobara try karo."
        )
        return

    link = message.text.strip()
    if "terabox" not in link:
        await message.reply_text("❌ Ye valid Terabox link nahi hai.")
        return

    # ⚠️ Abhi sirf demo reply (real downloader baad me add karenge)
    await message.reply_text(f"✅ Link mila: {link}\n\n(Download system abhi testing me hai.)")

print("✅ Bot Started Successfully!")

app.run()
