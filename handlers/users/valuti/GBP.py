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


@dp.message_handler(text='See how much a pound cost a year ago')
async def KursGBPGodnazad(message: types.Message):
    await message.answer(
        'Please wait ... Receiving information from <a href="https://finance.yahoo.com/">'
        + "Yahoo Finance" + '</a>')
    await message.answer('British pound sterling 🇬🇧\n'
                         + 'A year ago, you could have bought British pound sterling for' +
                         str(round(yf.download('GBPRUB=X', str(now.year - 1) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + ' ₽', reply_markup=perexodigbps)
