from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.AkciiKeyboard import AkciyaKey
from loader import dp
import datetime
from states.test import Test
import yfinance as yf
from aiogram.dispatcher import FSMContext

now = datetime.datetime.now()

if len(str(now.month)) == 1:
    nowm = '0' + str(now.month)
if len(str(now.day)) == 1:
    nowd = '0' + str(now.day)


@dp.message_handler(text='Learn share prices', state=None)
async def menuakcii(message: types.Message):
    await message.answer('To get started, enter the ticker of the stock that interests you.',
                         reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()


@dp.message_handler(text='Посмотреть цену другой акции', state=None)
async def menuakqwqeqcii(message: types.Message):
    await message.answer('To get started, enter the ticker of the stock that interests you.',
                         reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    data = await state.get_data()
    answer1 = data.get("answer1")
    print(answer1)
    await message.answer(
        'Wait... Receiving information from <a href="https://finance.yahoo.com/">'
        + "Yahoo Finance" + '</a>')
    await message.answer(
        f'Today you can buy a share of the company {answer1.upper()} for ' + str(round(
            yf.download(answer1.upper(), f'{now.year}-{now.month}-{now.day - 1}')['Adj Close'][
                0])) + '$',
        reply_markup=AkciyaKey)
    await state.finish()
