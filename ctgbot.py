import telebot
from requests import get
# import randint
bot = telebot.TeleBot('7506431083:AAGd8EAO2DPEMbvYghhqH3ezJ9QT-90NrEs')

from telebot import types

# bot.user_data = {}

# dict_ = {
#   'x + 27 = 58' : '31',
#   '32 + x = 76' : '44',
#   '64 – x = 27' : '37',
#   'x – 16 = 73' : '89',
#   '720 : с = 80' : '9',
#   '68 – 3 • с = 59' : '3',
#   '55 : (25 : х) = 11' : '5',
#   '(х - 50) • 4 = 200' : '100',
#   '888 – 15: х = 885' : '5',
#   'Х : 4 = 84 + 16' : '400',

#   'x - (133 + 75) = 32' : '240',
#   '0,7x - 0,2x = 5,5' : '11',
#   '2,1 • 4 - 6y = -42' : '7',
#   '10x + 15 = 7x + 6' : '-3'
# }

# data = list(dict_.items())

# counter = 0

@bot.message_handler(commands=['start'])
def start(message):
    # Готовим кнопки
    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    # key_2 = types.InlineKeyboardButton(text='2 класс', callback_data='2-7_grade')
    # # И добавляем кнопку на экран
    # keyboard.add(key_2)
    # key_3 = types.InlineKeyboardButton(text='3 класс', callback_data='2-7_grade')
    # keyboard.add(key_3)
    # key_4 = types.InlineKeyboardButton(text='4 класс', callback_data='2-7_grade')
    # keyboard.add(key_4)
    key_5 = types.InlineKeyboardButton(text='5 класс', callback_data='2-7_grade')
    keyboard.add(key_5)
    key_6 = types.InlineKeyboardButton(text='6 класс', callback_data='2-7_grade')
    keyboard.add(key_6)
    key_7 = types.InlineKeyboardButton(text='7 класс', callback_data='2-7_grade')
    keyboard.add(key_7)
#     key_8 = types.InlineKeyboardButton(text='8 класс', callback_data='8_garde')
#     keyboard.add(key_8)
#     key_9 = types.InlineKeyboardButton(text='9 класс', callback_data='9_grade')
#     keyboard.add(key_9)
#     key_10 = types.InlineKeyboardButton(text='10 класс', callback_data='10_grade')
#     keyboard.add(key_10)
#     key_11 = types.InlineKeyboardButton(text='11 класс', callback_data='11_grade')
#     keyboard.add(key_11)
    
    # Показываем все кнопки сразу и пишем сообщение о выборе message.from_user.id
    # dem = bot.send_message(message.from_user.id, 'lflflf')
    bot.send_message(message.from_user.id, text='Выбери свой класс', reply_markup=keyboard)
    # bot.register_next_step_handler(dem, callback_worker)


# @bot.message_handler(content_types=['text'])
# def start_message(message):
#     global z = 'Реши x + 27 = 58'
#     if message.text == '2':
#         bot.send_message(message.chat.id, 'Реши x + 27 = 58' )
        # if message.text == '31':
        #     bot.send_message(message.chat.id, 'ok')
        # elif message.text != '31':
        #     bot.send_message(message.chat.id, 'no')




# @bot.message_handler(content_types=['text'])
# def send_text(message):

#     if message.text == '31':
#         bot.send_message(message.chat.id, 'ok')
#     elif message.text != '31':
#         bot.send_message(message.chat.id, 'no')




# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "2-7_grade":
#         example, answer = data[randint(0, len(data - 1))]
#         bot.user_data[call.message.chat.id] = answer
#         bot.send_message(call.message.chat.id, example)



@bot.callback_query_handler(func = lambda call: True)

def callback_worker(call):
    # chat_id = call.chat.id
    # if call.data == "2-7_grade": 
    # ans = bot.send_message(call.from_user.id, 'Отлично! A теперь введите команду /first_test, чтобы начать')
        # exit()
    # Отправляем текст в Телеграм
    # lem = bot.send_message(call.from_user.id, 'lflflf')
    # bot.send_message(call.message.chat.id, ans)  
    bot.send_message(call.from_user.id, 'Отлично! A теперь введите команду /first_test, чтобы начать входное тестирование')
    
      
@bot.message_handler(commands=['first_test'])
def point0(message):
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    ans = bot.send_message(chat_id, 'Ваше первое задание: \nx + 27 = 58')
    
    bot.register_next_step_handler(ans, point1)
    
score = 0
counter = 0

def point1(message):
    # counter = 0
    # кто нам написал? узнаем id чата!
    global counter
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '31':
        counter = counter + 1 
        ans = bot.send_message(chat_id, 'Хорошо, ваше второе задание: \n32 + x = 76')
        bot.register_next_step_handler(ans, point2)
    else:
        ans = bot.send_message(message.chat.id, 'Хорошо, ваше второе задание: \n32 + x = 76')
        bot.register_next_step_handler(ans, point2)
        
        
        
def point2(message):
    # кто нам написал? узнаем id чата!
    global counter

    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '44':
        counter = counter + 1
        ans = bot.send_message(chat_id, 'Хорошо, ваше третье задание: \n64 – x = 27')
        bot.register_next_step_handler(ans, point3)
    else:
        ans = bot.send_message(chat_id, 'Хорошо, ваше третье задание: \n64 – x = 27')
    
        bot.register_next_step_handler(ans, point3)
        
        
def point3(message):
    # кто нам написал? узнаем id чата!
    global counter
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '37':
        counter = counter + 1
        ans = bot.send_message(chat_id, 'Четвертое задание: \nx – 16 = 73')
        bot.register_next_step_handler(ans, point4)
    else:
        ans = bot.send_message(chat_id, 'Четвертое задание: \nx – 16 = 73')
    
        bot.register_next_step_handler(ans, point4)
        
        
def point4(message):

    # кто нам написал? узнаем id чата!
    global counter
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '89':
        counter = counter + 1
        ans = bot.send_message(chat_id, 'Пятое задание: \n720 : с = 80')
        bot.register_next_step_handler(ans, point5)
    else:
        ans = bot.send_message(chat_id, 'Пятое задание: \n720 : с = 80')
    
        bot.register_next_step_handler(ans, point5)
        
def point5(message):
    # кто нам написал? узнаем id чата!
    global counter
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '9':
        counter = counter + 1
        ans = bot.send_message(chat_id, 'Шестое задание: \n68 – 3 • с = 59')
        # score = bot.send_message(chat_id, f"Вы набрали {counter} баллов")
        bot.register_next_step_handler(ans, point6)
    else:
        ans = bot.send_message(chat_id, 'Шестое задание: \68 – 3 • с = 59')
    
        bot.register_next_step_handler(ans, point6)
        
        
        
def point6(message):
    # кто нам написал? узнаем id чата!
    global counter
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '3':
        counter = counter + 1
        ans = bot.send_message(chat_id, 'Седьмое задание: \n55 : (25 : х) = 11')
        bot.register_next_step_handler(ans, point7)
    else:
        ans = bot.send_message(chat_id, 'Седьмое задание: \n55 : (25 : х) = 11')
    
        bot.register_next_step_handler(ans, point7)
        
        
        
        
def point7(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '5':
        counter += 1
        ans = bot.send_message(chat_id, 'Восьмое задание: \n(х - 50) • 4 = 200')
        bot.register_next_step_handler(ans, point8)
    else:
        ans = bot.send_message(chat_id, 'Восьмое задание: \n(х - 50) • 4 = 200')
        bot.register_next_step_handler(ans, point8)
        
        
        
def point8(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '100':
        counter += 1
        ans = bot.send_message(chat_id, 'Девятое задание: \n888 – 15: х = 885')
        bot.register_next_step_handler(ans, point9)
    else:
        ans = bot.send_message(chat_id, 'Девятое задание: \n888 – 15: х = 885')
        bot.register_next_step_handler(ans, point9)
        
        
        
        
        
def point9(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '5':
        counter += 1
        ans = bot.send_message(chat_id, 'Десятое задание: \nХ : 4 = 84 + 16')
        bot.register_next_step_handler(ans, point10)
    else:
        ans = bot.send_message(chat_id, 'Десятое задание: \nХ : 4 = 84 + 16')
        bot.register_next_step_handler(ans, point10)
        
        
        
        
        
def point10(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '400':
        counter += 1
        ans = bot.send_message(chat_id, 'Одиннадцатое задание: \nx - (133 + 75) = 32')
        bot.register_next_step_handler(ans, point11)
    else:
        ans = bot.send_message(chat_id, 'Одиннадцатое задание: \nx - (133 + 75) = 32')
        bot.register_next_step_handler(ans, point11)
        
        
def point11(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '240':
        counter += 1
        ans = bot.send_message(chat_id, 'Двенадцатое задание: \n0,7x - 0,2x = 5,5')
        bot.register_next_step_handler(ans, point12)
    else:
        ans = bot.send_message(chat_id, 'Двенадцатое задание: \n0,7x - 0,2x = 5,5')
        bot.register_next_step_handler(ans, point12)
        
        

def point12(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '11':
        counter += 1
        ans = bot.send_message(chat_id, 'Тринадцатое задание: \n2,1 • 4 - 6y = -42')
        bot.register_next_step_handler(ans, point13)
    else:
        ans = bot.send_message(chat_id, 'Тринадцатое задание: \n2,1 • 4 - 6y = -42')
        bot.register_next_step_handler(ans, point13)
        
        
        
        
def point13(message):
    global counter 
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '8,4' or text == '8.4':
        counter += 1
        ans = bot.send_message(chat_id, 'Четырнадцатое задание: \n10x + 15 = 7x + 6')
        bot.register_next_step_handler(ans, point14)
    else:
        ans = bot.send_message(chat_id, 'Четырнадцатое задание: \n10x + 15 = 7x + 6')
        bot.register_next_step_handler(ans, point14)
        
        
        
        
def point14(message):
    global counter 
    global score
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # что написали? узнаем текст входящего сообщения
    # по сути это замена input
    text = message.text
    if text == '-3':
        counter += 1
        bot.send_message(chat_id, 'Тестирование окончено!')
        # score = bot.send_message(chat_id, f"Ваши баллы: {counter}")
    else:
        bot.send_message(chat_id, 'Тестирование окончено!')
        # score = bot.send_message(chat_id, f"Ваши баллы: {counter}")    #f"Ваши баллы: {counter}"
        

    equations_img = open('linear_equations_multiply.jpg', 'rb')
    if counter < 12:
        bot.send_message(chat_id, f"Ваши баллы: {counter}. Вам следует изучить теорию ⬇️")
        # bot.send_message(score)
        bot.send_photo(chat_id, equations_img)
    if 12 <= counter < 14:
        bot.send_message(chat_id, f"Ваши баллы: {counter}. Отлично, но вам следует быть внимательнее с арифметикой")
    if counter == 14:
        bot.send_message(chat_id, f"Ваши баллы: {counter}. Ну просто заМУРчательно!")
        


# def score_results(message):
#     global score
#     chat_id = message.chat.id
#     equations_img = open('linear_equations_multiply.jpg', 'rb')
#     if counter < 12:
#         score = bot.send_message(chat_id, f"Ваши баллы: {counter}. Вам следует изучить теорию ⬇️")
#         bot.send_message(message.chat.id, score)
#         bot.send_photo(message.chat.id, equations_img)
        
               
# # @bot.message_handler(commands=['multiply_eq'])
# def tips_multiply(message):
#     equations_img = open('linear_equations_multiply.jpg', 'rb')
#     bot.send_photo(message.chat.id, equations_img)
        
      
      
bot.polling(none_stop=True, interval=0)