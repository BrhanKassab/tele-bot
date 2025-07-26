import time
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# استبدل التوكن بالتوكن الحقيقي تبعك
TOKEN = '7565454126:AAGBizkfjd1ME6kertOrpSLOtLlkKERskPo'

def extract_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print("[INFO] Sleeping 10 seconds to bypass protection...")
        time.sleep(10)

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return [f"فشل التحميل، كود الحالة: {response.status_code}"]

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select('a[href*="https://go.cimanow.cc"]')

        if not links:
            return ["لم يتم العثور على روابط تحميل في الصفحة."]

        return [link['href'] for link in links]

    except Exception as e:
        return [f"حدث خطأ أثناء جلب الصفحة: {e}"]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أرسل لي رابط صفحة الفيلم من cimanow.cc لأعطيك روابط التحميل.")

def handle_message(update: Update, context: CallbackContext):
    url = update.message.text.strip()

    if "cimanow.cc" not in url:
        update.message.reply_text("الرجاء إرسال رابط من موقع cimanow.cc فقط.")
        return

    update.message.reply_text("جاري استخراج روابط التحميل، يرجى الانتظار...")

    links = extract_links(url)
    for link in links:
        update.message.reply_text(link)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(MessageHandler(None, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
