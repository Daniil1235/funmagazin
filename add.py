import strings
from main import bot, types


def m(message: types.Message):
    bot.delete_message(message.chat.id, message.id)
    text = message.text.split(" ")[1]
    name = message.text.split(" ")[2]
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(strings.Button.yes, callback_data=f'addcart {text} {name}')
    btn2 = types.InlineKeyboardButton(strings.Button.no, callback_data='delmsg')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, strings.add_warning + name + strings.add_warning2, reply_markup=markup)





