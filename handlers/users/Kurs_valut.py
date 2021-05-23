from aiogram import types
from loader import dp
import datetime
from keyboards.default.KursKeyboard import perexodieuro, perexodiusd, perexodigbps
import yfinance as yf

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day)
m = x + '-' + y + '-' + z
print(m)


@dp.message_handler(text='💵')
async def kursUSA(message: types.Message):
    await message.answer('Wait... Receiving information from <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('USD 🇺🇸\n'
                         + 'Today you can buy a dollar for' +
                         str(round(yf.download('RUB=X', str(now.year) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0]))
                         + '₽', reply_markup=perexodiusd)


@dp.message_handler(text='💶')
async def KursEuro(message: types.Message):
    await message.answer('Wait... Receiving information from <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Euro 🇪🇺\n' +
                         'Today you can buy euros for ' + str(
        round(yf.download('EURRUB=X', str(now.year) + '-' + str(now.month) +
                          '-' + str(now.day))['Adj Close'][0])) +
                         '₽', reply_markup=perexodieuro)


@dp.message_handler(text='💷')
async def KursEuro(message: types.Message):
    await message.answer('Please wait ... Receiving information from <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('🇬🇧\n' +
                         'Today you can buy pound for ' + str(
        round(yf.download('GBPRUB=X', str(now.year) + '-' + str(now.month) +
                          '-' + str(now.day))['Adj Close'][0])) +
                         '₽', reply_markup=perexodigbps)
