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
            KeyboardButton(text='Back to menu')
        ],
    ],
    resize_keyboard=True
)

perexodieuro = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='See how much the euro cost a year ago')
        ],
        [
            KeyboardButton(text='Back to currency selection')
        ],
    ],
    resize_keyboard=True
)

perexodiusd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='See how much a dollar cost a year ago')
        ],
        [
            KeyboardButton(text='Back to currency selection')
        ],
    ],
    resize_keyboard=True
)

perexodigbps = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='See how much a pound cost a year ago')
        ],
        [
            KeyboardButton(text='Back to currency selection')
        ],
    ],
    resize_keyboard=True
)
