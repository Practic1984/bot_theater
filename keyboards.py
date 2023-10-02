from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID

def main_menu_user():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Расписание", callback_data="schedule"),
        InlineKeyboardButton("Стоимость", callback_data="price"),
        InlineKeyboardButton("Записаться", url=f"https://t.me/MagicBodyy"),
        InlineKeyboardButton("Наши тренировки", callback_data="workout"),
        InlineKeyboardButton("Наши отзывы", url='https://yandex.ru/maps/org/magic_body/120738172326/reviews/?ll=37.879773%2C55.697222&mode=search&sctx=ZAAAAAgBEAAaKAoSCXV4COOn8UJAEXu9%2B%2BO92EtAEhIJDf5%2BMVuyqj8RjxmojH%2BfkT8iBgABAgMEBSgKOABA8lNIAWIrcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9FbmFibGVCZWF1dHlGaWx0ZXI9MWoCcnWdAc3MTD2gAQCoAQC9AXmrR0DCAQamm7nkwQPqAQDyAQD4AQCCAiTRhNC40YLQvdC10YEg0YHRgtGD0LTQuNGPIG1hZ2ljIGJvZHmKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=37.879773%2C55.697222&sspn=0.026071%2C0.008604&tab=reviews&text=%D1%84%D0%B8%D1%82%D0%BD%D0%B5%D1%81%20%D1%81%D1%82%D1%83%D0%B4%D0%B8%D1%8F%20magic%20body&z=16'),
        InlineKeyboardButton("Как нас найти?", callback_data="adress"),
        )
    return markup

def menu_workout():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Женское здоровье", callback_data="1"),
        InlineKeyboardButton("Силовая тренировка", callback_data="2"),
        InlineKeyboardButton("Стретчинг", callback_data="3"),
        InlineKeyboardButton("Хатха-Йога", callback_data="4"),
        InlineKeyboardButton("High Heels", callback_data="5"),
        InlineKeyboardButton("Аэростретчинг", callback_data="6"),
        InlineKeyboardButton("Назад", callback_data="back"),
    )

    return markup


def lets_go():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("Приступим?", callback_data="lets_go"),

        )
    return markup


def choice_cat(list_cat):
    markup = InlineKeyboardMarkup()
    for i in list_cat:
        markup.add(
            InlineKeyboardButton(i, callback_data=f"looser::category::{i}"),
             )
    # markup.add(
    #         InlineKeyboardButton('В главное меню', callback_data=f"begin"),
    #          )
    return markup

def text_to_time_menegment():
    markup = InlineKeyboardMarkup()

    markup.add(
            InlineKeyboardButton('Добавить цель', callback_data=f"begin"),
            InlineKeyboardButton('Формировать расписание', callback_data=f"run_schedule"),
             )

    return markup
def result_marcup():
    markup = InlineKeyboardMarkup()

    markup.add(
            InlineKeyboardButton('Запланировать следующую неделю', callback_data=f"begin"),
             )
    return markup
def del_schedule():
    markup = InlineKeyboardMarkup()

    markup.add(
            InlineKeyboardButton('Приступить', callback_data=f"begin"),
             )
    return markup


def run_schedule():
    markup = InlineKeyboardMarkup()
    markup.add(
            InlineKeyboardButton('Стереть', callback_data=f"del_schedule"),
            InlineKeyboardButton('Сохранить', callback_data=f"go_time_menegment"),
             )
    return markup

def choice_target(list_tar):
    markup = InlineKeyboardMarkup()
    for i in list_tar:
        markup.add(
            InlineKeyboardButton(i, callback_data=f"looser::target::{i}"),
             )
    # markup.add(
    #         InlineKeyboardButton('В главное меню', callback_data=f"begin"),
    #          )
    return markup


def choice_event_on_day():
    markup = InlineKeyboardMarkup()
    markup.add(
            InlineKeyboardButton('Пн', callback_data=f"Пн"),
            InlineKeyboardButton('Вт', callback_data=f"Вт"),
            InlineKeyboardButton('Ср', callback_data=f"Ср"),
            InlineKeyboardButton('Чт', callback_data=f"Чт"),
            InlineKeyboardButton('Пт', callback_data=f"Пт"),
             )
    return markup

def choose_event_day(list):
    markup = InlineKeyboardMarkup()
    for i in list:
        text_btn = i.split('::')[2]
        callback_btn = i
        markup.add(
                InlineKeyboardButton(text_btn, callback_data=callback_btn)
                )
    return markup

def main_menu_moder():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Выгрузить пользователей", callback_data="get_users"),
        InlineKeyboardButton("Изменить расписание", callback_data="change_schedule"),
        )
    return markup
