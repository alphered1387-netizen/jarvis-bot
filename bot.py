import os
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text

        response = client.responses.create(
            model="gpt-5-mini",
            input=user_text
        )

        await update.message.reply_text(response.output_text)

    except Exception as e:
        await update.message.reply_text("یه مشکلی پیش اومد 😅 دوباره امتحان کن.")

app = Application.builder().token(
    os.environ["TELEGRAM_BOT_TOKEN"]
).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

app.run_polling()
