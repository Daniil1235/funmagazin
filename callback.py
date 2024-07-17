import sqlite3
import strings
from main import bot, types


def m(callback: types.CallbackQuery):
    if callback.data == "clear":
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(f'UPDATE users SET cart = "[]" WHERE id= "{callback.message.chat.id}"')
        bot.send_message(callback.message.chat.id, strings.cart_clear)
        connection.commit()
        cursor.close()
        connection.close()

    elif "order" in callback.data:
        cart = eval(callback.data.replace("order ", ""))
        s = strings.order_list + callback.message.chat.first_name + ": \n"
        for i in cart:
            s += i + "\n"
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(strings.Button.accept, callback_data=f"yes {callback.message.chat.id}")
        btn2 = types.InlineKeyboardButton(strings.Button.decline, callback_data=f"no {callback.message.chat.id}")
        markup.row(btn1, btn2)
        bot.delete_message(callback.message.chat.id, callback.message.id)
        bot.send_message(5645569833, s, reply_markup=markup)

    elif "yes" in callback.data:
        id = callback.data.split(" ")[1]
        bot.send_message(id, strings.accepted)
        bot.edit_message_text(strings.end, callback.message.chat.id, callback.message.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(strings.Button.done, callback_data=f"done {id}"))
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=markup)

    elif "no" in callback.data:
        bot.send_message(callback.data.split(" ")[1], strings.order_declined)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=None)
        bot.send_message(callback.message.chat.id, strings.declined)

    elif "done" in callback.data:
        bot.send_message(callback.data.split(" ")[1], strings.done)
        bot.delete_message(callback.message.chat.id, callback.message.id)
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(f'UPDATE users SET cart = "[]" WHERE id= "{callback.data.split(" ")[1]}"')
        bot.send_message(callback.message.chat.id, strings.cart_clear)
        connection.commit()
        cursor.close()
        connection.close()

    elif "getsum" in callback.data:
        bot.send_message(callback.message.chat.id, strings.wait)
        bot.send_message(5645569833, callback.data.split(" ")[1] + strings.want)

