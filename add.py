import sqlite3

import strings
from main import bot, types


def m(message: types.Message):
    bot.delete_message(message.chat.id, message.id)
    text = message.text.replace("/add ", "")
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT cart FROM users WHERE id={message.from_user.id}")
    cart = eval(cursor.fetchone()[0])
    try:
        cursor.execute(f"SELECT name FROM items WHERE id={text}")
        name = cursor.fetchone()[0]
        cart.append(name)
        cursor.execute(f"SELECT sum FROM users WHERE id={message.from_user.id}")
        sum = cursor.fetchone()[0]
        cursor.execute(f"SELECT price FROM items WHERE id={text}")
        price = int(cursor.fetchone()[0])
        if sum >= price:
            cursor.execute(f'UPDATE users SET cart="{cart}" WHERE id="{message.from_user.id}"')
            bot.send_message(message.chat.id, strings.add_success)
            sum -= price
            cursor.execute(f'UPDATE users SET sum="{sum}" WHERE id="{message.from_user.id}"')
        else:
            bot.send_message(message.chat.id, strings.money_error)
    except Exception:
        bot.send_message(message.chat.id, strings.add_error)
        return


    connection.commit()
    cursor.close()
    connection.close()
