from telegram import Update
from telegram.ext import ContextTypes
import datetime


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'hello\n/time\n/sum\n/help')


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg_items = update.message.text.split()
    x = int(msg_items[1])
    y = int(msg_items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_path = 'logs.csv'
    with open(file_path, 'a') as file:
        file.write(
            f'{datetime.datetime.now().time()},{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
