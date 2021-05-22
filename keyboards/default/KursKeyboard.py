from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kursvalue = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💵')
        ],
        [
            KeyboardButton(text='💶')
        ],
        [
            KeyboardButton(text='💷')
        ],
        [
            KeyboardButton(text='Вернуться в меню')
        ],
    ],
    resize_keyboard=True
)

perexodieuro = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Посмотреть сколько стоило евро год назад')
        ],
        [
            KeyboardButton(text='Вернуться к выбору валюты')
        ],
    ],
    resize_keyboard=True
)

perexodiusd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Посмотреть сколько стоил доллар год назад')
        ],
        [
            KeyboardButton(text='Вернуться к выбору валюты')
        ],
    ],
    resize_keyboard=True
)

perexodigbps = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Посмотреть сколько стоил фунт год назад')
        ],
        [
            KeyboardButton(text='Вернуться к выбору валюты')
        ],
    ],
    resize_keyboard=True
)
