from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage()

key = os.getenv('token')
bot = Bot(token=key)

dp = Dispatcher(bot, storage=storage)
