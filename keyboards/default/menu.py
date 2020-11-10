from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuswe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Узнать котировки акций')
        ],
        [
            KeyboardButton(text='Узнать курс валют')
        ],
        [
            KeyboardButton(text='Войти в свой дневник расходов')
        ],
    ],
    resize_keyboard=True
)
