from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menuswe
from keyboards.default.KursKeyboard import kursvalue
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        'Добро пожаловать в FinanceBot!\n\nДля начала работы определите свой запрос.',
        reply_markup=menuswe)


@dp.message_handler(text='Вернуться в меню')
async def bot_start(message: types.Message):
    await message.answer(
        'Добро пожаловать в FinanceBot!\n\nДля начала работы определите свой запрос.',
        reply_markup=menuswe)


@dp.message_handler(text='Узнать курс валют' or 'Вернуться к выбору валюты')
async def kurs(message: types.Message):
    await message.answer('Выберите интересующую вас валюту.\n\nВсе данные предоставлены'
                         ' <a href="https://finance.yahoo.com/">' + "Yahoo Finance" + '</a>',
                         reply_markup=kursvalue)


@dp.message_handler(text='Вернуться к выбору валюты')
async def kurs(message: types.Message):
    await message.answer('Выберите интересующую вас валюту.\n\nВсе данные предоставлены'
                         ' <a href="https://finance.yahoo.com/">' + "Yahoo Finance" + '</a>',
                         reply_markup=kursvalue)

