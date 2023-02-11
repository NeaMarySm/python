from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
import tic_tac_toe as t
import tic_main as tm
import random


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'hello\n/time\n/sum\n/help')


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.now()}')


async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg_items = update.message.text.split()
    x = int(msg_items[1])
    y = int(msg_items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    play_field = tm.field
    bot = tm.bot
    user = tm.user
    current = user
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}! Let`s play tic-tac-toe!')
    await update.message.reply_text(t.print_field(play_field))
    if random.randint(0, 1) == 0:
        current = bot
    if current == bot:
        await update.message.reply_text(f'I`ll start. I`m playing with {bot}.')
    else:
        await update.message.reply_text(f'You are the first. {user} are yours! /put [cell_number]')


# async def gaming(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     msg = update.message.text.split()
#     cell = int(msg[1])
#     while (t.is_playing(play_field)):
#         if current == user:
#             await update.message.reply_text(f'Choose a cell! /put =cell_number=')
#             await update.message.reply_text(t.print_field(play_field))
#             while not t.number_check(cell, play_field):
#                 await update.message.reply_text(f'Wrong value! Choose a cell!')
#         else:
#             cell = t.bot_cell(play_field)
#             await update.message.reply_text(f'My turn! I`ll put {bot} in cell {cell} ')
#         t.make_step(cell, play_field, current)
#         current = t.change_player(current, user, bot)
#         await update.message.reply_text(t.print_field(play_field))
#     if current == user:
#         await update.message.reply_text(f'I won.')
#     else:
#         await update.message.reply_text(f'Congratulations! You are the winner!')


async def time_to_new_year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_year = datetime(2024, 1, 1, 0, 0, 0)
    today = datetime.now()
    delta = new_year-today
    days_left = delta.days
    minutes, seconds = divmod(delta.seconds, 60)
    hours, minutes = divmod(minutes, 60)

    await update.message.reply_text(f'To New Year left {days_left} days, {hours} hours, {minutes} minutes, {seconds} seconds')


def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_path = 'logs.csv'
    with open(file_path, 'a') as file:
        file.write(
            f'{datetime.now()},{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
