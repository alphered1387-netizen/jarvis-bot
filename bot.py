import os
from google import genai
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=update.message.text
        )

        await update.message.reply_text(response.text)

    except Exception:
        await update.message.reply_text(
            "یه مشکلی پیش اومد 😅 دوباره امتحان کن."
        )

app = Application.builder().token(
    os.environ["TELEGRAM_BOT_TOKEN"]
).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

app.run_polling()
