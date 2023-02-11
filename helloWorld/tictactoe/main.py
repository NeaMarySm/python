import functions as fn
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

user = 'X'
bot = 'O'
current_player = user
fn.print_field(field)

while (fn.is_playing(field)):
    if current_player == user:
        fn.user_step(current_player, field)
        current_player = bot
    else:
        fn.bot_step(field, current_player)
        current_player = user
    fn.print_field(field)

if current_player == user:
    print(f'Bot is won!')
else:
    print(f'User is won!')
