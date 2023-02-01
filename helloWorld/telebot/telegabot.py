from telegram.ext import ApplicationBuilder, CommandHandler
import commands as cm
import functions as fn

token = fn.get_token('token_husky_tasky_bot.txt')
app = ApplicationBuilder().token(
    token).build()
print('server start')

app.add_handler(CommandHandler("hello", cm.hello))
app.add_handler(CommandHandler("time", cm.time))
app.add_handler(CommandHandler("help", cm.help))
app.add_handler(CommandHandler("sum", cm.sum))
app.run_polling()
print('server stop')
