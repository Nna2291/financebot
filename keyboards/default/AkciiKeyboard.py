from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

AkciyaKey = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Посмотреть цену другой акции')
        ],
    ],
    resize_keyboard=True
)
