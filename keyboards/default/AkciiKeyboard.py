from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

AkciyaKey = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Посмотреть цену другой акции')
        ],
        [
            KeyboardButton(text='Back to currency selection')
        ],
    ],
    resize_keyboard=True
)
