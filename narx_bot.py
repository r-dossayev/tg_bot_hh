import urllib
from io import BytesIO

import telebot
from telebot import types
from collections import defaultdict

# Replace 'your_bot_token' with your actual bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
PAYMENT_TOKEN = "5420394252:TEST:543267"  # TODO edit
# Replace 'your_paymaster_token' with your actual PayMaster token
# PAYMASTER_TEST_TOKEN = '1744374395:TEST:75a0ae907a8479b70d96'

bot = telebot.TeleBot(BOT_TOKEN)

products = {
    '1': {'name': 'Pancakes', 'price': 1000, 'description': 'Delicious pancakes with maple syrup.', 'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '2': {'name': 'Круассан', 'price': 500, 'description': 'Flaky croissant with a buttery taste.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '3': {'name': 'Bubble tea: Oreo', 'price': 1500, 'description': 'Refreshing bubble tea with Oreo flavor.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '4': {'name': 'Bubble tea: Sakura', 'price': 1100, 'description': 'Cherry blossom flavored bubble tea.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '5': {'name': 'Bubble tea: Blue matcha', 'price': 1200, 'description': 'Blue matcha infused bubble tea.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '6': {'name': 'Bubble tea: Green matcha', 'price': 1100, 'description': 'Green matcha flavored bubble tea.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '7': {'name': 'Bubble tea: Nutella', 'price': 1000, 'description': 'Indulgent bubble tea with Nutella.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '8': {'name': 'Cake: Vupipai', 'price': 2000,
          'description': 'Delightful Vupipai cake with layers of sweetness.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '9': {'name': 'Cake: Tiramisu', 'price': 2000, 'description': 'Classic Tiramisu cake with coffee flavor.',
          'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '10': {'name': 'Cake: Qulpynai', 'price': 1900, 'description': 'Exquisite Qulpynai cake with a unique twist.',
           'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
    '11': {'name': 'Cake: Oreo', 'price': 2000, 'description': 'Irresistible Oreo cake with cookie goodness.',
           'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwU2B0lgeZJV_L50_2ihdecmmotRgNXWA1Tg&usqp=CAU'},
}
# Dictionary to track selected products and their quantities
selected_products = defaultdict(int)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    markup.row(button1)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)


@bot.message_handler(content_types='text')
def handle_text(message):
    if message.text == '🛍 Товары':
        show_products(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.message:
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        if call.data.startswith('add_to_cart'):
            product_id = call.data.split('#')[1]
            selected_products[product_id] += 1
            bot.answer_callback_query(call.id, f'Товар #{product_id} добавлен в корзину!')
        elif call.data == 'checkout':
            checkout(chat_id, message_id)
        elif call.data == 'cancel_checkout':
            bot.edit_message_text('Оформление заказа отменено.', chat_id, message_id)
            selected_products.clear()
        elif call.data == 'confirm_checkout':
            confirm_checkout(chat_id, message_id)
            selected_products.clear()  # Clear the cart after confirming the order
        elif call.data.startswith('details_product'):
            product_id = call.data.split('#')[1]
            selected_products[product_id] += 1
            dd2 = BytesIO(urllib.request.urlopen(products.get(product_id).get("photo")).read())
            # dd2 = BytesIO(urllib.request.urlopen("https://example.com/croissant.jpg"))
            ff = types.InlineKeyboardMarkup()
            ff.add(types.InlineKeyboardButton("kupit", callback_data=f'add_to_cart#{product_id}'))
            bot.send_photo(chat_id, caption=products.get(product_id).get("description"), photo=dd2, reply_markup=ff)

            bot.answer_callback_query(call.id, f'Товар #{product_id} добавлен в корзину!')


def show_products(chat_id):
    markup = types.InlineKeyboardMarkup()

    for product_id, info in products.items():
        markup.add(
            types.InlineKeyboardButton(f'{info["name"]} - {info["price"]} ₸',
                                       callback_data=f'details_product#{product_id}'))

    markup.add(types.InlineKeyboardButton('Перейти к оформлению заказа', callback_data='checkout'))

    bot.send_message(chat_id, 'Выберите товар:', reply_markup=markup)


def checkout(chat_id, message_id):
    markup = types.InlineKeyboardMarkup()

    total_amount = 0
    for product_id, quantity in selected_products.items():
        product_name = get_product_name_by_id(product_id)
        product_price = get_product_price_by_id(product_id)
        total_amount += quantity * product_price

        markup.add(types.InlineKeyboardButton(f'{product_name} x{quantity}', callback_data=f'dummy_callback'))

    markup.add(types.InlineKeyboardButton(f'Итого: {total_amount} ₸', callback_data='dummy_callback'))
    markup.add(types.InlineKeyboardButton('Подтвердить заказ', callback_data='confirm_checkout'))
    markup.add(types.InlineKeyboardButton('Отменить заказ', callback_data='cancel_checkout'))

    bot.edit_message_text('Ваш заказ:', chat_id, message_id, reply_markup=markup)


def confirm_checkout(chat_id, message_id):
    total_amount = 0
    prices = []
    for product_id, quantity in selected_products.items():
        product_price = get_product_price_by_id(product_id)
        product_name = get_product_name_by_id(product_id)
        total_amount += quantity * product_price
        prices.append(types.LabeledPrice(label=product_name, amount=quantity * product_price * 100))
        bot.send_invoice(chat_id, "Оплата", "товары", "payload", PAYMENT_TOKEN, "KZT", prices)
    # paymaster_url = f'https://paymaster.kz/test?token={PAYMASTER_TEST_TOKEN}&amount={5000}&description=Order&currency=KZT'
    # bot.edit_message_text(f'Оплатить заказ на сумму ₸ {total_amount}.', chat_id, message_id,
    #                       reply_markup=types.InlineKeyboardMarkup().add(
    #                           types.InlineKeyboardButton('Оплатить', url=paymaster_url)))


def get_product_name_by_id(product_id):
    products = {
        '1': 'Pancakes',
        '2': 'Круассан',
        '3': 'Bubble tea: Oreo',
        '4': 'Bubble tea: Sakura',
        '5': 'Bubble tea: Blue matcha',
        '6': 'Bubble tea: Green matcha',
        '7': 'Bubble tea: Nutella',
        '8': 'Cake: Vupipai',
        '9': 'Cake: Tiramisu',
        '10': 'Cake: Qulpynai',
        '11': 'Cake: Oreo',
    }
    return products.get(product_id, f'Unknown Product #{product_id}')


def get_product_price_by_id(product_id):
    prices = {
        '1': 1000,
        '2': 500,
        '3': 1500,
        '4': 1100,
        '5': 1200,
        '6': 1100,
        '7': 1000,
        '8': 2000,
        '9': 2000,
        '10': 1900,
        '11': 2000,
    }
    return prices.get(product_id, 0)


bot.polling(none_stop=True)

#
# import telebot
# import config
#
# snn = ''
# pidm = 0
# tel = ''
# jobNameId = 0
# newJobName = ''
# newJobVacId = 0
# bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
# from telebot import types
#
# dd = types.ReplyKeyboardMarkup(resize_keyboard=True)
# dd.add('/about')
# dd.add('/profile')
# dd.add('/newJob')
# dd.add('/cats')
#
#
# def newJobInputs(message):
#     global pidm
#     bot.send_message(message.chat.id, text="Siz Usyngan Jumys kay kalada?")
#     pidm = message.id
#
#
# def newJobInputsName(message):
#     global jobNameId
#     bot.send_message(message.chat.id, text="Siz Usyngan Jumys Atauy?")
#     jobNameId = message.id
#
#
# def phone(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_phone = types.KeyboardButton(text="Send phone", request_contact=True)
#     keyboard.add(button_phone)
#     bot.send_message(message.chat.id, 'Тел номер жіберіңіз!', reply_markup=keyboard)
#
#
# @bot.message_handler(content_types=['contact'])
# def contact(message):
#     global tel
#     if message.contact is not None:
#         tel = message.contact.phone_number
#         bot.send_message(message.chat.id, text="Номеріңіз сәтті тіркелді!", reply_markup=dd)
#         # selectCateg(message)
#
#
# @bot.message_handler(commands=['test'])
# def start_message(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton(text='ҮШ', callback_data=3))
#     markup.add(telebot.types.InlineKeyboardButton(text='ТӨРТ', callback_data=4))
#     markup.add(telebot.types.InlineKeyboardButton(text='БЕС', callback_data=5))
#     bot.send_message(message.chat.id, text="Мектептегі орташа баҒаҢыз неше болды?", reply_markup=markup)
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id,
#                      "Салем, {0.first_name}!\n мен - <b>{1.first_name}</b> Narxoz жайлы ақпарат беретін ботпын \nBailanys : /about \nProfile : /profile \njai test: /test\njumys kosu: /newJob\nJumys izdeu: /cats".format(
#                          message.from_user, bot.get_me()),
#                      parse_mode='html', reply_markup=dd)
#
#
# @bot.message_handler(commands=['about'])
# def about(mes):
#     markups = telebot.types.InlineKeyboardMarkup()
#     markups.add(telebot.types.InlineKeyboardButton(text='Admin Github', url='https://github.com/mallemes'))
#     markups.add(telebot.types.InlineKeyboardButton(text='Admin telegram', url='https://t.me/mallemes'))
#
#     bot.send_message(mes.chat.id, text="Adminmen Bailanys", reply_markup=markups)
#
#
# @bot.message_handler(commands=['newJob'])
# def newJob(message):
#     mukup_inline = types.InlineKeyboardMarkup()
#     item_yes = types.InlineKeyboardButton(text='Иә', callback_data='yes')
#     item_no = types.InlineKeyboardButton(text='Жоқ', callback_data='no')
#     mukup_inline.add(item_yes, item_no)
#     bot.send_message(message.chat.id, 'Жалғастырасызба?', reply_markup=mukup_inline, timeout=3)
#
#
# @bot.message_handler(commands=['profile'])
# def profile(message):
#     # myJobs2 = dbExam.myJobs(message.from_user.id)
#     text = "Profile: " + message.from_user.first_name + "\n" + "   Men engizgen jumystar:  \n"
#     caunt22 = 1
#     # for i in myJobs2:
#     #     text = text + str(caunt22) + " Jumys aty: " + i[1] + " Jumys kala: " + i[0] + "\n"
#     #     caunt22 += 1
#     bot.send_message(message.chat.id, text=text)
#
#
# # @bot.message_handler(commands=['cats'])
# # def allCategories(messages):
# #     markup3 = telebot.types.InlineKeyboardMarkup()
# #     for i in dbExam.ret:
# #         markup3.add(telebot.types.InlineKeyboardButton(text=i[0], callback_data="#catVacs" + str(i[1])))
# #     bot.send_message(messages.chat.id, text="Біздегі бар вакансиялардың категориялары!", reply_markup=markup3)
#
#
# @bot.message_handler(content_types=['text'])
# def textController(message):
#     global snn
#     global newJobName
#     if message.chat.type == 'private':
#         if message.text == 'test':
#             bot.send_message(message.chat.id, message)
#         elif message.text == 'about':
#             about(message)
#         # elif message.text == 'cats':
#         #     allCategories(message)
#         elif message.id == pidm + 2:
#             snn = message.text
#             newJobInputsName(message)
#         # elif message.id == jobNameId + 2:
#         #     newJobName = message.text
#         #     createNewJob(message)
#         else:
#             bot.send_message(message.chat.id, 'Белгісіз команда 😢')
#
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         answer = ' '
#         global newJobVacId
#         global tel
#         if call.message:
#             if call.data == '3':
#                 return about(mes=call.message)
#             elif call.data == '4':
#                 answer = 'MAMAN DIRECTOR BOLGANGO'
#                 bot.answer_callback_query(callback_query_id=call.id, text='Рахмет!')
#             elif call.data == '5':
#                 answer = 'OTIRIK AKPARAT'
#                 bot.answer_callback_query(callback_query_id=call.id, text='Рахмет!')
#             # elif call.data[0] == '#':
#             #     return myCatVacs2(call.message, int(call.data[8]))
#             # elif call.data[0] == '&':
#             #     return vacJobs(call.message, int(call.data[5:]))
#             # elif call.data[0] == '*':
#             #     return newJobVacs(call.message, int(call.data[8]))
#             # elif call.data[0] == '₸ ':
#             #     newJobVacId = int(call.data[5:])
#             #     return newJobInputs(call.message)
#             elif call.data == 'yes':
#                 phone(call.message)
#             elif call.data == 'no':
#                 bot.send_message(call.message.chat.id, "Пакеда!!! 👋")
#             # elif call.data == "???":
#             #     bot.send_message(chat_id=call.message.chat.id, text="inn jaz")
#             #     my_tel(call.message)
#
#             bot.send_message(call.message.chat.id, answer)
#     except Exception as e:
#         print(repr(e))
#
#
# # def myCatVacs2(message, g):
# #     markup4 = telebot.types.InlineKeyboardMarkup()
# #     for k in dbExam.myCatVacs(g):
# #         markup4.add(telebot.types.InlineKeyboardButton(text=k[2], callback_data="&Vacs" + str(k[0])))
# #     bot.send_message(message.chat.id, text="Сіз таңдаған категория бойынша вакансиялар!", reply_markup=markup4)
#
# #
# # def vacJobs(message, n):
# #     ss = 'СІЗ ТАҢДАҒАН ВАКАНСИЯ БОЙЫНША  ЖУМЫСТАР  \n'
# #     for x in dbExam.myVacJobs(n):
# #         f = f"  City: {x[1]} JobName: {x[2]} jobManager: {x[3]}  \n"
# #         ss = ss + str(f)
# #     bot.send_message(message.chat.id, str(ss))
#
#
# # def selectCateg(message):
# #     markup5 = telebot.types.InlineKeyboardMarkup()
# #     for i in dbExam.ret:
# #         markup5.add(telebot.types.InlineKeyboardButton(text=i[0], callback_data="*2catVac" + str(i[1])))
# #     bot.send_message(message.chat.id, text="Сіз енгізгіңіз келген жумыстың категориясын таңдаңыз!",
# #                      reply_markup=markup5)
#
#
# # def newJobVacs(message, g):
# #     markup6 = telebot.types.InlineKeyboardMarkup()
# #     for k in dbExam.myCatVacs(g):
# #         markup6.add(telebot.types.InlineKeyboardButton(text=k[2], callback_data="₸  Vacs" + str(k[0])))
# #     bot.send_message(message.chat.id, text="Сіз енгізгіңіз келген жумыстың ваканциясын таңдаңыз!", reply_markup=markup6)
#
#
# # def createNewJob(mess):
# #     global snn, tel, newJobVacId, newJobName
# #     ss22 = "https://t.me/" + str(tel)
# #     print(mess.from_user.id)
# #     myUz = mess.from_user.id
# #     dbExam.newJob(snn, newJobName, ss22, newJobVacId, myUz)
# #     bot.send_message(mess.chat.id, "Жумыс сәтті тіркелді көру ушін: /profile", parse_mode='html')
#
#
# # RUN
# bot.polling(none_stop=True, timeout=1)
