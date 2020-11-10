from aiogram import types
from loader import dp
import datetime

from keyboards.default.KursKeyboard import perexodigbps
import yfinance as yf

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day - 1)
m = x + '-' + y + '-' + z


@dp.message_handler(text='Посмотреть сколько стоил фунт месяц назад')
async def KursGBPVchera(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Фунт стерлингов Соединенного королевства 🇬🇧\n'
                         + 'Вчера вы могли купить фунт за ' +
                         str(round(yf.download('GBPRUB=X', str(now.year) + '-' + str(now.month - 1) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodigbps)


@dp.message_handler(text='Посмотреть сколько стоил фунт год назад')
async def KursGBPGodnazad(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Фунт стерлингов Соединенного королевства 🇬🇧\n'
                         + 'Год назад вы могли купить доллар за ' +
                         str(round(yf.download('GBPRUB=X', str(now.year - 1) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodigbps)
