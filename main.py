import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! پیام خود را بفرست تا به فرمت خاص با عکس پاسخ دهم.")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    text = message.text
    final_message = f"📌 *دسته‌بندی*: 🧠 فلسفه\n\n{text}\n\n#فلسفه #telegram"
    with open("image.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=final_message, parse_mode="Markdown")

bot.infinity_polling()
