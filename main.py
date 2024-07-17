from telebot import TeleBot, types
import config
import sqlite3
import strings

bot = TeleBot(config.BOT_TOKEN)

results = []
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM items")
items = cursor.fetchall()
for i in items:
    results.append(types.InlineQueryResultArticle(
        id=f'{i[0]}', title=f"{i[1]}",
        description=f"{strings.amount} {i[2]}\n"
                    f"{strings.price} {i[3]}",
        thumbnail_url=f"https://daniil1235.github.io/bot-photo/images/{i[0]}.png",
        input_message_content=types.InputTextMessageContent(
            message_text=f"/add {i[0]}")))

import abcd
import callback
import add
import shop
import cart
import strings


lang = ""

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    connection.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                      (id TEXT, 
                      sum INTEGER,
                      cart TEXT,
                      lang varchar(3))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS items 
                      (id INTEGER PRIMARY KEY, 
                      name VARCHAR(30), 
                      amount INTEGER, 
                      price VARCHAR(10), 
                      photo TEXT)""")

    connection.commit()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    exists = False
    for i in users:
        pass
        if i[1] == str(message.from_user.id):
            exists = True

    connection.commit()
    cursor.close()
    connection.close()
    code = message.text.replace("/start ", "")
    if code == "123488":
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        if not exists:
            cursor.execute(f'INSERT INTO users(id, sum, cart) VALUES ("{message.from_user.id}", "0", "[]")')
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🇷🇺 русский", callback_data="rus"))
            markup.add(types.InlineKeyboardButton("🇬🇧 english", callback_data="eng"))
            bot.send_message(message.chat.id, "Выберете язык/select language", reply_markup=markup)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        if not exists:
            bot.send_message(message.chat.id, strings.login_error)


@bot.callback_query_handler(func=lambda call: True)
def callbackk(call):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    callback.m(call)


@bot.message_handler(commands=["add"])
def addd(message):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    add.m(message)


@bot.message_handler(commands=["shop"])
def shopp(message):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    shop.m(message)


@bot.message_handler(commands=["cart"])
def cartt(message):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    cart.m(message)


@bot.message_handler(commands=["sum"])
def sum(message: types.Message):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT sum FROM users WHERE id = {message.from_user.id}")
    sum = str(cursor.fetchone()[0])
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(strings.Button.get_sum, callback_data=f"getsum {message.from_user.first_name}"))
    bot.send_message(message.chat.id, strings.your_sum + sum, reply_markup=markup)


@bot.inline_handler(func=lambda query: True)
def query_text(query: types.InlineQuery):
    global lang
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = {message.chat.id}")
    lang = cursor.fetchone()[0]

    text = query.query
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    global results
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    r = []
    for i in items:
        if text in i[1]:
            for q in results:
                if int(q.id) == i[0]:
                    r.append(q)
    bot.answer_inline_query(query.id, r)


bot.polling(none_stop=True)
