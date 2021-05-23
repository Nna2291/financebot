from aiogram import types
from loader import dp
import datetime

from keyboards.default.KursKeyboard import perexodiusd
import yfinance as yf

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day - 1)
m = x + '-' + y + '-' + z


@dp.message_handler(text='See how much a dollar cost a year ago')
async def KursUSDGodnazad(message: types.Message):
    await message.answer(
        'Please wait ... Receiving information from <a href="https://finance.yahoo.com/">'
        + "Yahoo Finance" + '</a>')
    await message.answer('USD 🇺🇸\n'
                         + 'A year ago, you could have bought a dollar for ' +
                         str(round(yf.download('RUB=X', str(now.year - 1) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodiusd)
