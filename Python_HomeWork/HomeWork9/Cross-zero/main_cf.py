import os
import random
import sys

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import strings as st


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5648533896:AAGpQkZC2ggTj7_MQsz43WDzLn3r_Yr-v5M").build()

app.add_handler(CommandHandler("hello", hello))
print('server ok')

app.run_polling()