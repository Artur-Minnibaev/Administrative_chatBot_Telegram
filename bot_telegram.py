import time

from warning import text

from control_bot import bot, dp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
from database import sqlite_db
from database.sqlite_db import create_profile, edit_profile
from aiogram.dispatcher.filters import Text
import os, json, string

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


async def on_startup(_):
    await sqlite_db.sql_start()
    print('Bot online!')


HELP_TEXT = text


class FSMAdmin(StatesGroup):
    user_id = State()
    name = State()
    tg_id = State()
    phone_number = State()
    number_apt = State()


@dp.message_handler(content_types=['new_chat_members'])
async def handler_new_member(message: types.Message):
    name = message.new_chat_members[0].username
    if name == None:
        message_info = await bot.send_message(message.chat.id, text=HELP_TEXT, parse_mode='HTML')
        await asyncio.sleep(120)
        await message_info.delete()
    elif name == name:
        message_info = await bot.send_message(message.chat.id, text=HELP_TEXT, parse_mode='HTML')
        await asyncio.sleep(120)
        await message_info.delete()


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        warning = await message.reply("Маты запрещены!\nKötü sözler yasaklandı")
        await message.delete()
        await asyncio.sleep(15)
        await warning.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
