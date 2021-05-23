from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuswe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Learn share prices')
        ],
        [
            KeyboardButton(text='Find out the exchange rate')
        ],
    ],
    resize_keyboard=True
)
