import telebot
from telebot import types
import time
import datetime
from datetime import timedelta
from requests import Session

bot = telebot.TeleBot('токен')


def perevod_vremeni():
    dt_now = datetime.datetime.now()  # data today
    w_day = dt_now.weekday()  # week day
    res_dt = ''  # date from monday

    if w_day == 0:
        res_dt = dt_now
    elif w_day == 1:
        res_dt = dt_now - timedelta(days=1)
    elif w_day == 2:
        res_dt = dt_now - timedelta(days=2)
    elif w_day == 3:
        res_dt = dt_now - timedelta(days=3)
    elif w_day == 4:
        res_dt = dt_now - timedelta(days=4)
    elif w_day == 5:
        res_dt = dt_now - timedelta(days=5)
    elif w_day == 6:
        res_dt = dt_now - timedelta(days=6)

    date_time = datetime.datetime(int((str((res_dt.date())).split('-'))[0]),
                                  int((str((res_dt.date())).split('-'))[1]),
                                  int((str((res_dt.date())).split('-'))[2]), 00, 00)

    mon_date = str(int((time.mktime(date_time.timetuple())))) + '000'  # id monday !!!!

    res_dt = res_dt + timedelta(days=5)
    date_time = datetime.datetime(int((str((res_dt.date())).split('-'))[0]),
                                  int((str((res_dt.date())).split('-'))[1]),
                                  int((str((res_dt.date())).split('-'))[2]), 23, 59, 59)

    sun_date = str(int((time.mktime(date_time.timetuple())))) + '999'  # id sunday !!!!
    return mon_date, sun_date


def get_biol():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://belgorod.vsopen.ru/app/add/studentDiary',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': '***',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '***',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    m_date, s_date = perevod_vremeni()

    params = {
        'startDate': m_date,
        'stopDate': s_date,
        'eduYearId': '***',
        '_': '***',
    }

    data = {'redirect': '', 'login': 'логин', 'password': 'пароль'}

    work = Session()

    resp = work.get('https://belgorod.vsopen.ru/app/login?loginerror&redirect_url=', headers=headers)

    res = work.post('https://belgorod.vsopen.ru/app/login?loginerror&redirect_url=', headers=headers, data=data,
                    allow_redirects=True)

    result1 = work.post('https://belgorod.vsopen.ru/app/add/studentDiary', headers=headers)

    response = work.get(
        'https://belgorod.vsopen.ru/app/api/1/persons/394704/lessons',
        params=params,
        headers=headers,

    )

    itog = []
    count_qweqw = 0
    trt = []
    for i in response.json()['entities']:
        count_qweqw = count_qweqw + 1
        # print(i)
        lesson_name = i['subject']['name']
        lesson_hw = i['homework']
        lesson_links = []
        lesson_l = i['homeworkFiles']
        if len(lesson_l) != 0:
            for j in lesson_l:
                lesson_links.append(j['link'])
        lesson = [lesson_name, lesson_hw, lesson_links]
        trt.append(lesson)
        # print(lesson)
        if (count_qweqw == 9) or (count_qweqw == 17) or (count_qweqw == 25) or (count_qweqw == 32) or (
                count_qweqw == 39):
            itog.append(trt)
            trt = []

    dni = ['*Понедельник*', '*Вторник*', '*Среда*', '*Четверг*', '*Пятница*', '*Суббота*']

    answer = ''

    for i in range(len(itog)):
        answer = answer + str(dni[i]).upper() + '\n'
        answer = answer + ('\n')
        popi = itog[i]
        for er in popi:
            for u in range(3):
                rt = er[u]
                if rt == '' or rt == None:
                    pass
                elif u == 0:
                    rt = '🏫 ' + '*' + str(rt).upper() + '*'
                    answer = answer + (str(rt) + '\n')
                elif u == 1:
                    rt = '📒 ' + '*' + rt + '*'
                    answer = answer + (str(rt) + '\n')
                elif u == 2:
                    for y in rt:
                        rer = '👉 [ссылка](' + y + ')'
                        answer = answer + (str(rer) + ' ')
                    answer = answer + '\n'
                else:
                    answer = answer + (str(rt) + '\n')
            answer = answer + ('\n')
        answer = answer + 'FFFFF' + '\n'
        answer = answer + ('\n')
    if answer.split('FFFFF') == ['']:
        return ['каникулы', 'каникулы', 'каникулы', 'каникулы', 'каникулы']
    else:
        return answer.split('FFFFF')


def get_json():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://belgorod.vsopen.ru/app/add/studentDiary',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': '***',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '***"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    m_date, s_date = perevod_vremeni()

    params = {
        'startDate': m_date,
        'stopDate': s_date,
        'eduYearId': '***',
        '_': '***',
    }

    data = {'redirect': '', 'login': 'лоигн', 'password': 'пароль'}

    work = Session()

    resp = work.get('https://belgorod.vsopen.ru/app/login?loginerror&redirect_url=', headers=headers)

    res = work.post('https://belgorod.vsopen.ru/app/login?loginerror&redirect_url=', headers=headers, data=data,
                    allow_redirects=True)

    result1 = work.post('https://belgorod.vsopen.ru/app/add/studentDiary', headers=headers)

    response = work.get(
        'https://belgorod.vsopen.ru/app/api/1/persons/531118/lessons',
        params=params,
        headers=headers,

    )

    # print(response.text)

    itog = []
    count_qweqw = 0
    trt = []
    for i in response.json()['entities']:
        count_qweqw = count_qweqw + 1
        # print(i)
        lesson_name = i['subject']['name']
        lesson_hw = i['homework']
        lesson_links = []
        lesson_l = i['homeworkFiles']
        if len(lesson_l) != 0:
            for j in lesson_l:
                lesson_links.append(j['link'])
        lesson = [lesson_name, lesson_hw, lesson_links]
        trt.append(lesson)
        # print(lesson)
        if count_qweqw == 8:
            count_qweqw = 0
            itog.append(trt)
            trt = []

    dni = ['*Понедельник*', '*Вторник*', '*Среда*', '*Четверг*', '*Пятница*', '*Суббота*']

    answer = ''

    for i in range(len(itog)):
        answer = answer + str(dni[i]).upper() + '\n'
        answer = answer + ('\n')
        popi = itog[i]
        for er in popi:
            for u in range(3):
                rt = er[u]
                if rt == '' or rt == None:
                    pass
                elif u == 0:
                    rt = '🏫 ' + '*' + str(rt).upper() + '*'
                    answer = answer + (str(rt) + '\n')
                elif u == 1:
                    rt = '📒 ' + '*' + rt + '*'
                    answer = answer + (str(rt) + '\n')
                elif u == 2:
                    for y in rt:
                        rer = '👉 [ссылка](' + y + ')'
                        answer = answer + (str(rer) + ' ')
                    answer = answer + '\n'
                else:
                    answer = answer + (str(rt) + '\n')
            answer = answer + ('\n')
        answer = answer + 'FFFFF' + '\n'
        answer = answer + ('\n')
    if answer.split('FFFFF') == ['']:
        return ['каникулы', 'каникулы', 'каникулы', 'каникулы', 'каникулы']
    else:
        return answer.split('FFFFF')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
    btn1 = types.KeyboardButton('айти')
    btn2 = types.KeyboardButton('химбио')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text='''Привет, {0.first_name}!

Меня зовут Альберт. Я бот. Каждый день я просыпаюсь с надеждой, что хотя бы сегодня ты начнёшь делать домашку. Если я не отвечаю на твои сообщения, значит скорее всего мне поплохело от твоих оценок. Просто напиши @yaroslaveq и я снова буду в строю. Чтобы начать наш разговор заново, отправь  /start . 

Теперь, когда мы знакомы, ты можешь выбрать свою касту👇'''.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'айти':
        user_id = message.chat.id
        print(user_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        bytn1 = types.KeyboardButton('пн👾')
        bytn2 = types.KeyboardButton('вт👾')
        bytn3 = types.KeyboardButton('ср👾')
        bytn4 = types.KeyboardButton('чт👾')
        bytn5 = types.KeyboardButton('пт👾')
        markup.add(bytn1, bytn2, bytn3, bytn4, bytn5)
        bot.send_message(message.chat.id,
                         text="Выбери день недели👇".format(
                             message.from_user), reply_markup=markup)

    elif message.text == 'пн👾':
        bot.send_message(message.from_user.id,
                         get_json()[0],
                         parse_mode='Markdown')
    elif message.text == 'вт👾':
        bot.send_message(message.from_user.id,
                         get_json()[1],
                         parse_mode='Markdown')
    elif message.text == 'ср👾':
        bot.send_message(message.from_user.id,
                         get_json()[2],
                         parse_mode='Markdown')
    elif message.text == 'чт👾':
        bot.send_message(message.from_user.id,
                         get_json()[3],
                         parse_mode='Markdown')
    elif message.text == 'пт👾':
        bot.send_message(message.from_user.id,
                         get_json()[4],
                         parse_mode='Markdown')


    elif message.text == 'химбио':
        user_id = message.chat.id
        print(user_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        bytn1 = types.KeyboardButton('пн🧪')
        bytn2 = types.KeyboardButton('вт🧪')
        bytn3 = types.KeyboardButton('ср🧪')
        bytn4 = types.KeyboardButton('чт🧪')
        bytn5 = types.KeyboardButton('пт🧪')
        markup.add(bytn1, bytn2, bytn3, bytn4, bytn5)
        bot.send_message(message.chat.id,
                         text="Выбери день недели👇".format(
                             message.from_user), reply_markup=markup)

    elif message.text == 'пн🧪':
        bot.send_message(message.from_user.id,
                         get_biol()[0],
                         parse_mode='Markdown')
    elif message.text == 'вт🧪':
        bot.send_message(message.from_user.id,
                         get_biol()[1],
                         parse_mode='Markdown')
    elif message.text == 'ср🧪':
        bot.send_message(message.from_user.id,
                         get_biol()[2],
                         parse_mode='Markdown')
    elif message.text == 'чт🧪':
        bot.send_message(message.from_user.id,
                         get_biol()[3],
                         parse_mode='Markdown')
    elif message.text == 'пт🧪':
        bot.send_message(message.from_user.id,
                         get_biol()[4],
                         parse_mode='Markdown')
    else:
        bot.send_message(message.from_user.id, 'ты тупой? нажми на кнопку! или пиши /start',
                         parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)  
