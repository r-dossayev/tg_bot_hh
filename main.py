import random
import telebot
import config
import dbExam

snn = ''
pidm = 0
tel = ''
jobNameId = 0
newJobName = ''
newJobVacId = 0
bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
from telebot import types

dd = types.ReplyKeyboardMarkup(resize_keyboard=True)
dd.add('/about')
dd.add('/profile')
dd.add('/newJob')
dd.add('/cats')


def newJobInputs(message):
    global pidm
    bot.send_message(message.chat.id, text="Siz Usyngan Jumys kay kalada?")
    pidm = message.id


def newJobInputsName(message):
    global jobNameId
    bot.send_message(message.chat.id, text="Siz Usyngan Jumys Atauy?")
    jobNameId = message.id


def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Send phone", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Тел номер жіберіңіз!', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    global tel
    if message.contact is not None:
        tel = message.contact.phone_number
        bot.send_message(message.chat.id, text="Номеріңіз сәтті тіркелді!", reply_markup=dd)
        selectCateg(message)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='ҮШ', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='ТӨРТ', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='БЕС', callback_data=5))
    bot.send_message(message.chat.id, text="Мектептегі орташа баҒаҢыз неше болды?", reply_markup=markup)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Салем, {0.first_name}!\n мен - <b>{1.first_name}</b> студенттерге жумыс табуга комектесетін ботпын\nBailanys : /about \nProfile : /profile \njai test: /test\njumys kosu: /newJob\nJumys izdeu: /cats".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=dd)


@bot.message_handler(commands=['about'])
def about(mes):
    markups = telebot.types.InlineKeyboardMarkup()
    markups.add(telebot.types.InlineKeyboardButton(text='Admin Github', url='https://github.com/mallemes'))
    markups.add(telebot.types.InlineKeyboardButton(text='Admin telegram', url='https://t.me/mallemes'))

    bot.send_message(mes.chat.id, text="Adminmen Bailanys", reply_markup=markups)


@bot.message_handler(commands=['newJob'])
def newJob(message):
    mukup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Иә', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Жоқ', callback_data='no')
    mukup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Жалғастырасызба?', reply_markup=mukup_inline, timeout=3)


@bot.message_handler(commands=['profile'])
def profile(message):
    myJobs2 = dbExam.myJobs(message.from_user.id)
    text = "Profile: " + message.from_user.first_name + "\n" + "   Men engizgen jumystar:  \n"
    caunt22 = 1
    for i in myJobs2:
        text = text + str(caunt22) + " Jumys aty: " + i[1] + " Jumys kala: " + i[0] + "\n"
        caunt22 += 1
    bot.send_message(message.chat.id, text=text)


@bot.message_handler(commands=['cats'])
def allCategories(messages):
    markup3 = telebot.types.InlineKeyboardMarkup()
    for i in dbExam.ret:
        markup3.add(telebot.types.InlineKeyboardButton(text=i[0], callback_data="#catVacs" + str(i[1])))
    bot.send_message(messages.chat.id, text="Біздегі бар вакансиялардың категориялары!", reply_markup=markup3)


@bot.message_handler(content_types=['text'])
def textController(message):
    global snn
    global newJobName
    if message.chat.type == 'private':
        if message.text == 'test':
            bot.send_message(message.chat.id, message)
        elif message.text == 'about':
            about(message)
        elif message.text == 'cats':
            allCategories(message)
        elif message.id == pidm + 2:
            snn = message.text
            newJobInputsName(message)
        elif message.id == jobNameId + 2:
            newJobName = message.text
            createNewJob(message)
        else:
            bot.send_message(message.chat.id, 'Белгісіз команда 😢')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        answer = ' '
        global newJobVacId
        global tel
        if call.message:
            if call.data == '3':
                return about(mes=call.message)
            elif call.data == '4':
                answer = 'MAMAN DIRECTOR BOLGANGO'
                bot.answer_callback_query(callback_query_id=call.id, text='Рахмет!')
            elif call.data == '5':
                answer = 'OTIRIK AKPARAT'
                bot.answer_callback_query(callback_query_id=call.id, text='Рахмет!')
            elif call.data[0] == '#':
                return myCatVacs2(call.message, int(call.data[8]))
            elif call.data[0] == '&':
                return vacJobs(call.message, int(call.data[5:]))
            elif call.data[0] == '*':
                return newJobVacs(call.message, int(call.data[8]))
            elif call.data[0] == '$':
                newJobVacId = int(call.data[5:])
                return newJobInputs(call.message)
            elif call.data == 'yes':
                phone(call.message)
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, "Пакеда!!! 👋")
            # elif call.data == "???":
            #     bot.send_message(chat_id=call.message.chat.id, text="inn jaz")
            #     my_tel(call.message)

            bot.send_message(call.message.chat.id, answer)
    except Exception as e:
        print(repr(e))


def myCatVacs2(message, g):
    markup4 = telebot.types.InlineKeyboardMarkup()
    for k in dbExam.myCatVacs(g):
        markup4.add(telebot.types.InlineKeyboardButton(text=k[2], callback_data="&Vacs" + str(k[0])))
    bot.send_message(message.chat.id, text="Сіз таңдаған категория бойынша вакансиялар!", reply_markup=markup4)


def vacJobs(message, n):
    ss = 'СІЗ ТАҢДАҒАН ВАКАНСИЯ БОЙЫНША  ЖУМЫСТАР  \n'
    for x in dbExam.myVacJobs(n):
        f = f"  City: {x[1]} JobName: {x[2]} jobManager: {x[3]}  \n"
        ss = ss + str(f)
    bot.send_message(message.chat.id, str(ss))


def selectCateg(message):
    markup5 = telebot.types.InlineKeyboardMarkup()
    for i in dbExam.ret:
        markup5.add(telebot.types.InlineKeyboardButton(text=i[0], callback_data="*2catVac" + str(i[1])))
    bot.send_message(message.chat.id, text="Сіз енгізгіңіз келген жумыстың категориясын таңдаңыз!",
                     reply_markup=markup5)


def newJobVacs(message, g):
    markup6 = telebot.types.InlineKeyboardMarkup()
    for k in dbExam.myCatVacs(g):
        markup6.add(telebot.types.InlineKeyboardButton(text=k[2], callback_data="$Vacs" + str(k[0])))
    bot.send_message(message.chat.id, text="Сіз енгізгіңіз келген жумыстың ваканциясын таңдаңыз!", reply_markup=markup6)


def createNewJob(mess):
    global snn, tel, newJobVacId, newJobName
    ss22 = "https://t.me/" + str(tel)
    print(mess.from_user.id)
    myUz = mess.from_user.id
    dbExam.newJob(snn, newJobName, ss22, newJobVacId, myUz)
    bot.send_message(mess.chat.id, "Жумыс сәтті тіркелді көру ушін: /profile", parse_mode='html')


# RUN
bot.polling(none_stop=True, timeout=1)
