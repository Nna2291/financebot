from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.AkciiKeyboard import AkciyaKey
from loader import dp
import datetime
from states.test import Test
import yfinance as yf
from aiogram.dispatcher import FSMContext

now = datetime.datetime.now()
x = str(now.year)
y = str(now.month)
z = str(now.day)
m = x + '-' + y + '-' + z



@dp.message_handler(text='Узнать котировки акций', state=None)
async def menuakcii(message: types.Message):
    await message.answer('Для начала работы введитие тиккер акции, которая вас интересует.',
                         reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()


@dp.message_handler(text='Посмотреть цену другой акции', state=None)
async def menuakqwqeqcii(message: types.Message):
    await message.answer('Для начала работы введитие тиккер акции, которая вас интересует.',
                         reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    data = await state.get_data()
    answer1 = data.get("answer1")
    await message.answer('Подождите... Идет получение информации от <a href="https://finance.yahoo.com/">'
                         + "Yahoo Finance" + '</a>')
    await message.answer('Сейчас акции ' + answer1 + ' можно купить за ' +
                         str(round(yf.download(answer1, str(now.year) + '-' + str(now.month) +
                                               '-' + str(now.day))['Adj Close'][0])) + ' $',
                         reply_markup=AkciyaKey)
    await state.finish()
