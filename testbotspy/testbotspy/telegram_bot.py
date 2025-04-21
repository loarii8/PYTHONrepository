from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "YOUR_BOT_API_KEY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm your Telegram bot 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if 'joke' in msg:
        reply = random.choice(["Why did the bot cross the road? To train on the other side!", "I'm not lazy, I'm just in sleep mode."])
    elif 'your name' in msg:
        reply = "I'm your cool little Telegram chatbot!"
    else:
        reply = "I'm still learning but I'm happy to chat!"
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
