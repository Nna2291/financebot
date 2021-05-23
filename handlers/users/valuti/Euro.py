from aiogram import types
from loader import dp
import datetime
from keyboards.default.KursKeyboard import perexodieuro
import yfinance as yf

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day)
m = x + '-' + y + '-' + z


@dp.message_handler(text='See how much the euro cost a year ago')
async def KursEuroGodnazad(message: types.Message):
    await message.answer(
        'Please wait ... Receiving information from <a href="https://finance.yahoo.com/">'
        + "Yahoo Finance" + '</a>')
    await message.answer('Евро 🇪🇺\n' +
                         'A year ago, you could buy euros for ' + str(
        round(yf.download('EURRUB=X', str(now.year - 1) + '-' + str(now.month) +
                          '-' + str(now.day))['Adj Close'][0])) +
                         '₽', reply_markup=perexodieuro)
