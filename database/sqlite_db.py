import sqlite3
from control_bot import bot, dp

base = sqlite3.connect('lavinya_tomuk')
cursor = base.cursor()


async def sql_start():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY, name, tg_id, phone_number, number_apt)')
    base.commit


async def create_profile(user_id):
    user = cursor.execute("SELECT 1 FROM users WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        base.commit()


async def edit_profile(state, user_id):
            async with state.proxy() as data:
                cursor.execute("UPDATE users SET name = '{}', tg_id = '{}', phone_number = '{}', number_apt = '{}' WHERE user_id == '{}'".format(
                    data['name'], data['tg_id'], data['phone_number'], data['number_apt'], user_id))
            base.commit()