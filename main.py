from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "7565454126:AAGBizkfjd1ME6kertOrpSLOtLlkKERskPo"

def start(update, context):
    update.message.reply_text("أهلاً! أرسل لي رابط فيلم من موقع cimanow.cc لأعطيك روابط التحميل.")

def handle_message(update, context):
    text = update.message.text
    # هنا ممكن تضيف كود استخراج روابط التحميل حسب موقع cimanow.cc
    update.message.reply_text(f"وصلني الرابط: {text}\nبس السكربت لسه ما فعل استخراج الروابط.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
