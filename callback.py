import sqlite3

import strings
from main import bot, types, inlineupdate
from strings import get_money2

giveid = ""


def m(callback: types.CallbackQuery):
    global giveid
    if callback.data == "clear":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
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
        # bot.edit_message_text(strings.end, callback.message.chat.id, callback.message.id)
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
        connection.commit()
        cursor.close()
        connection.close()

    elif "getsum" in callback.data:
        bot.send_message(callback.message.chat.id, strings.wait)
        bot.send_message(5645569833, callback.data.split(" ")[1] + strings.want)

    elif "addcart" in callback.data:
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        text = callback.data.split(" ")[1]
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT cart FROM users WHERE id={callback.message.chat.id}")
        cart = eval(cursor.fetchone()[0])
        try:
            cursor.execute(f"SELECT name FROM items WHERE id={text}")
            name = cursor.fetchone()[0]
            cart.append(name)
            cursor.execute(f"SELECT sum FROM users WHERE id={callback.message.chat.id}")
            sum = cursor.fetchone()[0]
            cursor.execute(f"SELECT price FROM items WHERE id={text}")
            price = int(cursor.fetchone()[0])
            cursor.execute(f"SELECT amount FROM items WHERE id={text}")
            amount = int(cursor.fetchone()[0])
            if amount == 0:
                bot.send_message(callback.message.chat.id, strings.no_amount)
                return
            if sum >= price:
                cursor.execute(f'UPDATE users SET cart="{cart}" WHERE id="{callback.message.chat.id}"')
                bot.send_message(callback.message.chat.id, name + strings.add_success)
                sum -= price
                cursor.execute(f'UPDATE users SET sum="{sum}" WHERE id="{callback.message.chat.id}"')
                cursor.execute(f"SELECT amount FROM items WHERE id={text}")
                cursor.execute(f"UPDATE items SET amount ={amount - 1}")
            else:
                bot.send_message(callback.message.chat.id, strings.money_error)
        except KeyboardInterrupt:
            bot.send_message(callback.message.chat.id, strings.add_error)
            return
        connection.commit()
        cursor.close()
        connection.close()
        inlineupdate()


    elif callback.data == "delmsg":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


    elif "give" in callback.data:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT priv FROM users WHERE id={callback.data.split(' ')[2]}")
        priv = cursor.fetchone()
        if priv[0] != 1:
            bot.answer_callback_query(callback_query_id=callback.id, text=strings.admin_error, show_alert=True)
            return
        giveid = callback.data.split(" ")[1]
        bot.register_next_step_handler(callback.message, give)
        bot.send_message(callback.message.chat.id, strings.enter_sum)

        connection.commit()
        cursor.close()
        connection.close()


def give(message: types.Message):
    global giveid
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT sum FROM users WHERE id={giveid}")
    sum = int(cursor.fetchone()[0])
    sum += int(message.text)
    cursor.execute(f"UPDATE users SET sum={sum} WHERE id={giveid}")
    connection.commit()
    cursor.close()
    connection.close()
    bot.send_message(message.chat.id, strings.success)
    markup = types.InlineKeyboardMarkup()
    markup.add()
    bot.send_message(giveid, strings.get_money + message.text + get_money2)

