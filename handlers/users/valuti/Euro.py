from aiogram import types
from loader import dp
import datetime
from pycbrf.toolbox import ExchangeRates
from keyboards.default.KursKeyboard import perexodieuro
import yfinance as yf


now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day - 1)
m = x + '-' + y + '-' + z

now1 = datetime.datetime.now()
x = str(now.year - 1)
y = str(now.month)
z = str(now.day)
m1 = x + '-' + y + '-' + z

rates = ExchangeRates(m)
rates1 = ExchangeRates(m1)


@dp.message_handler(text='Посмотреть сколько стоил евро месяц назад')
async def KursEuroVchera(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Евро 🇪🇺\n' +
                         'Месяц назад вы могли купить евро за ' + str(
        round(yf.download('EURRUB=X', str(now.year) + '-' + str(now.month - 1) +
                          '-' + str(now.day))['Adj Close'][0])) +
                         '₽', reply_markup=perexodieuro)


@dp.message_handler(text='Посмотреть сколько стоило евро год назад')
async def KursEuroGodnazad(message: types.Message):
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Евро 🇪🇺\n' +
                         'Год назад вы могли купить евро за ' + str(
        round(yf.download('EURRUB=X', str(now.year - 1) + '-' + str(now.month) +
                          '-' + str(now.day))['Adj Close'][0])) +
                         '₽', reply_markup=perexodieuro)
