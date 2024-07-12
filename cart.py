from main import bot, types
import strings
import sqlite3


def m(message: types.Message):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT cart FROM users WHERE id={message.from_user.id}")
    cart = eval(cursor.fetchone()[0])
    if not cart:
        bot.send_message(message.chat.id, "Корзина пуста!")
        return
    s = strings.your_cart
    for i in cart:
        s += i + "\n"

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(strings.Button.order, callback_data=f"order {cart}")
    btn2 = types.InlineKeyboardButton(strings.Button.clearcart, callback_data=f"clear")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, s, reply_markup=markup)

    connection.commit()
    cursor.close()
    connection.close()