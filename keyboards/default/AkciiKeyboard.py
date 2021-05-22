from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

AkciyaKey = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Посмотреть цену другой акции')
        ],
        [
            KeyboardButton(text='Вернуться в меню')
        ],
    ],
    resize_keyboard=True
)
