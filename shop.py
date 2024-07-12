from main import bot, types
import strings


def m(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(strings.Button.search, switch_inline_query_current_chat=""))
    bot.send_message(message.chat.id, strings.search, reply_markup=markup)
