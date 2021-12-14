import datetime

import telebot  # pip install pyTelegramBotAPI
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import token
# from create_bd import create_db
import db_functions

import re


bot = telebot.TeleBot(token)


def gen_main_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Первые блюда", callback_data="/first_dishes"),
               InlineKeyboardButton("Вторые блюда", callback_data="/second dishes"),
               InlineKeyboardButton("Закуски", callback_data="/snacks"),
               InlineKeyboardButton("Напитки", callback_data="/drinks"),
               InlineKeyboardButton("Десерты", callback_data="/deserts"),
               InlineKeyboardButton("Мне повезет", callback_data="/roulette"))
    return markup


@bot.message_handler(commands=['start', 'main_menu'])
def start_message(message):
    bot.send_message(message.chat.id, "Чем займемся?", reply_markup=gen_main_markup())

# полный список из таблиц

def first_dish_list_str():
    first_dish_list = ''
    for i in db_functions.get_first_dish_list():
        first_dish_list += f'{i[1]}\n{i[2]}\n'
    return first_dish_list

def second_dish_list_str():
    second_dish_list = ''
    for i in db_functions.get_second_dish_list():
        second_dish_list += f'{i[1]}\n{i[2]}\n'
    return second_dish_list

def deserts_list_str():
    deserts_list = ''
    for i in db_functions.get_deserts_list():
        deserts_list += f'{i[1]}\n{i[2]}\n'
    return deserts_list

def snacks_list_str():
    snacks_list = ''
    for i in db_functions.get_snacks_list():
        snacks_list += f'{i[1]}\n{i[2]}\n'
    return snacks_list

def drinks_list_str():
    drinks_list = ''
    for i in db_functions.get_drinks_list():
        drinks_list += f'{i[1]}\n{i[2]}\n'
    return drinks_list

# рандомная запись

def rnd_first_dish_str():
    rnd_first_dish = ''
    for i in db_functions.rnd_first_dish():
        rnd_first_dish = f'{i[2]}\n{i[3]}\n'
    return rnd_first_dish

def rnd_second_dish_str():
    rnd_second_dish = ''
    for i in db_functions.rnd_second_dish():
        rnd_second_dish = f'{i[2]}\n{i[3]}\n'
    return rnd_second_dish

def rnd_deserts_str():
    rnd_deserts = ''
    for i in db_functions.rnd_deserts():
        rnd_deserts = f'{i[2]}\n{i[3]}\n'
    return rnd_deserts

def rnd_snacks_str():
    rnd_snacks = ''
    for i in db_functions.rnd_snacks():
        rnd_snacks = f'{i[2]}\n{i[3]}\n'
    return rnd_snacks

def rnd_drinks_str():
    rnd_drinks = ''
    for i in db_functions.rnd_drinks():
        rnd_drinks = f'{i[2]}\n{i[3]}\n'
    return rnd_drinks

# ======================== Главное меню ==================
def first_dish_names():
    first_dish_names = []
    for i in db_functions.get_first_dish_list():
        first_dish_names.append(i[1])
    return first_dish_names

# def second_dish_names():
#     second_dish_names = []
#     for i in db_functions.get_second_dish_list():
#         first_dish_names.append(i[1])
#     return second_dish_names

# def first_dish_markup():
#     markup = InlineKeyboardMarkup()
#     for ex in db_functions.get_first_dish_list():
#         markup.add(InlineKeyboardButton(f'{ex[1]}', callback_data=ex[1]))
#     return markup


# Обработчик нажатия на кнопки. Именно здесь заключена основная логика бота.
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global dish
    # Выводим список первых блюд
    if call.data == "/first_dishes":
        bot.send_message(
            call.message.chat.id,
            f'{first_dish_list_str()}'
        )
    
    elif call.data == "/second dishes":
        bot.send_message(
            call.message.chat.id,
            f'{second_dish_list_str()}'
        )

    elif call.data == "/deserts":
        bot.send_message(
            call.message.chat.id,
            f'{deserts_list_str()}'
        )

    elif call.data == "/snacks":
        bot.send_message(
            call.message.chat.id,
            f'{snacks_list_str()}'
        )

    elif call.data == "/drinks":
        bot.send_message(
            call.message.chat.id,
            f'{drinks_list_str()}'
        )

    elif call.data == "/roulette":
        bot.send_message(
            call.message.chat.id,
            f'{rnd_first_dish_str()}\n{rnd_second_dish_str()}\n{rnd_snacks_str()}\n{rnd_deserts_str()}\n{rnd_drinks_str()}'
            
        )

    # if call.data == "/first_dishes":
    #     dish = ''
    #     bot.send_message(
    #         call.message.chat.id,
    #         f'Выберите блюдо:',
    #         reply_markup = first_dish_markup()
    #     )
    #
    # elif call.data in first_dish_names():
    #     dish = call.data
    # bot.send_message(
    #     call.message.chat.id,
    #     f'Выбрано блюдо: {dish}'
    # )



    # Выводим спиок вторых блюд
    # elif call.data == "/gyms":
    #     # print(call)
    #     bot.send_message(
    #         call.message.chat.id,
    #         f'{gyms_list_str()}/main_menu'
    #     )


print('Bot in work....')
# create_db()
bot.polling(none_stop=True, interval=0)
