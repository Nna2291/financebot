from aiogram import types
from loader import dp
import datetime
from pycbrf.toolbox import ExchangeRates
from keyboards.default.KursKeyboard import perexodiusd
import yfinance as yf

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day - 1)
m = x + '-' + y + '-' + z


rates = ExchangeRates(m)


@dp.message_handler(text='Посмотреть сколько стоил доллар месяц назад')
async def KursUSDVchera(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Доллар США USD 🇺🇸\n'
                         + 'Месяц назад вы могли купить доллар за ' +
                         str(round(yf.download('RUB=X', str(now.year) + '-' + str(now.month - 1) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodiusd)


@dp.message_handler(text='Посмотреть сколько стоил доллар год назад')
async def KursUSDGodnazad(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Доллар США USD 🇺🇸\n'
                         + 'Год назад вы могли купить доллар за ' +
                         str(round(yf.download('RUB=X', str(now.year - 1) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodiusd)
