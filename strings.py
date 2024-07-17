import main

lang = main.lang




class Dict:
    login_error = {"rus": "ошибка входа",
                   "eng": "login error"}
    ok = {"rus": "ок",
          "eng": "ok"}
    search = {"rus": "Нажмите для поиска:",
              "eng": "press for search"}
    your_cart = {"rus": "Ваша корзина: \n",
                 "eng": "your cart"}
    add_error = {"rus": "Не найдено",
                 "eng": "not found"}
    add_success = {"rus": "Добавлено в корзину",
                   "eng": "added to cart"}
    money_error = {"rus": "недостаточно средств",
                   "eng": "you dont have enough money"}
    cart_clear = {"rus": "Корзина очищена",
                  "eng": "cart cleared"}
    order_list = {"rus": "Список заказов от ",
                  "eng": "orders list from "}
    accepted = {"rus": "✅заказ принят. Ожидайте",
                "eng": "✅order accepter. Please wait"}
    declined = {"rus": "❌заказ отклонён!",
                "eng": "❌order declined!"}
    order_declined = {"rus": "❌Ваш заказ отклонён",
                      "eng": "❌your order is declined"}
    done = {"rus": "🛒Заказ готов. Сейчас его доставят",
            "eng": "🛒order id done. Wait for delivery"}
    complete = {"rus": "✅доставлен",
                "eng": "✅delivered"}
    end = {"rus": "Завершить:",
           "eng": "end:"}
    your_sum = {"rus": "ваш счёт: ",
                "eng": "your cart sum"}
    wait = {"rus": "сейчас к вам подойдут",
            "eng": "wait for helper"}
    want = {"rus": " хочет пополнить счёт",
            "eng": " want get cart sum"}
    amount = {"rus": "В наличии:",
              "eng": "in stock: "}
    price = {"rus": "Цена:",
             "eng": "price:"}


login_error = Dict.login_error[lang]
ok = Dict.ok[lang]
search = Dict.search[lang]
your_cart = Dict.your_cart[lang]
add_error = Dict.add_error[lang]
add_success = Dict.add_success[lang]
money_error = Dict.money_error[lang]
cart_clear = Dict.cart_clear[lang]
order_list = Dict.order_list[lang]
accepted = Dict.accepted[lang]
declined = Dict.declined[lang]
order_declined = Dict.order_declined[lang]
done = Dict.done[lang]
complete = Dict.complete[lang]
end = Dict.end[lang]
your_sum = Dict.your_sum[lang]
wait = Dict.want[lang]
want = Dict.wait[lang]
amount = Dict.amount[lang]
price = Dict.price[lang]


class Button:
    search = "🔍поиск"
    order = "🛒заказать всё"
    clearcart = "🗑очистить всё"
    accept = "✅разрешить"
    decline = "❌запретить"
    done = "✅готово"
    get_sum = "💲пополнить счёт"
