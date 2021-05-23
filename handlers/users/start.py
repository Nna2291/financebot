from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menuswe
from keyboards.default.KursKeyboard import kursvalue
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        'Welcome to FinanceBot!\nTo get started, define your request.',
        reply_markup=menuswe)


@dp.message_handler(text='Back to menu')
async def bot_start(message: types.Message):
    await message.answer(
        'Welcome to FinanceBot!\nTo get started, define your request.',
        reply_markup=menuswe)


@dp.message_handler(text='Learn share prices' or 'Back to currency selection')
async def kurs(message: types.Message):
    await message.answer('Select the currency you are interested in.\n\nAll data provided'
                         ' <a href="https://finance.yahoo.com/">' + "Yahoo Finance" + '</a>',
                         reply_markup=kursvalue)


'''@dp.message_handler(text='Вернуться к выбору валюты')
async def kurs(message: types.Message):
    await message.answer('Select the currency you are interested in.\n\nAll data provided'
                         ' <a href="https://finance.yahoo.com/">' + "Yahoo Finance" + '</a>',
                         reply_markup=kursvalue)'''

