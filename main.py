#                                                         Imports
from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from datetime import datetime
from config import BOT_TOKEN, admin_id

import T10.messages_10t_1 as msg_10t_1
import T10.messages_10t_2 as msg_10t_2
import keyboards as kb
import T10.send_messages_10t as send_msg_10t

import sqlite3 as sql

from background import keep_alive

db = sql.connect('database.db')
cur = db.cursor()


async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                tg_id INTEGER,
                class_id TEXT DEFAULT '1',
                group_id INTEGER DEFAULT 1,
                isNotified INTEGER DEFAULT 0
                )""")    
    db.commit()

async def main():
    await send_message_cron()

async def on_startup(_):
    await db_start()
    
    # await msg_10t_1.create_subjects()
    # await msg_10t_2.create_subjects()
    # await msg_10t_1.start_db_1()
    # await msg_10t_2.start_db_2()

    await msg_10t_1.create_subjects()
    await msg_10t_1.add_subjects()
    await msg_10t_2.create_subjects()
    await msg_10t_2.add_subjects()


    print('Database started!')
    print('Bot started!')

class Form(StatesGroup):
    my_message = State()
    check_class = State()

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)


# ---------------------------------------------------- Notifications ---------------------------------------------------
# @dp.message_handler(commands=['webapp'])
# async def webapp(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     webapp = types.WebAppInfo("https://schedule-bot.netlify.app")
#     web = types.KeyboardButton('🔗 Расписание', web_app=webapp)
#     markup.add(web)
#     await bot.send_message(chat_id=message.chat.id, text='Привет! Нажми кнопку ниже, чтобы открыть сайт', reply_markup=markup)

@dp.message_handler(commands=['notify'])
async def notifications(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    on = types.InlineKeyboardButton('🔔 Включить оповещения', callback_data='on_notifications')
    off = types.InlineKeyboardButton('🔕 Выключить оповещения', callback_data='off_notifications')
    markup.add(on)
    markup.add(off)
    if message.from_user.id == message.chat.id:
        await bot.send_message(chat_id=message.chat.id,
                           text='Чтобы включить или выключить оповещения от бота, нажмите на кнопки ниже.',
                           reply_markup=markup)
    else:
        await bot.send_message(chat_id=message.chat.id, text="Данная функция работает только в личных сообщениях!")

async def notify_db(id, isNotified):
    cur.execute('UPDATE users SET isNotified = "{isNotified}" WHERE tg_id = "{id}"'.format(isNotified=isNotified, id=id))
    db.commit()

async def on_notify(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='✅ Успешно! Оповещения о расписании <i>включены</i>. <b>Они будут отправляться автоматически каждый день [Понедельник-Суббота] в 7:45.</b>',
                           parse_mode='html')


async def off_notify(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='✅ Успешно! Оповещения о расписании <i>выключены</i>. <b>Теперь они не будут больше приходить.</b>',
                           parse_mode='html')

async def send_message_cron():
    users_first = [row[0] for row in cur.execute('SELECT tg_id FROM users WHERE isNotified = "{isNotified}" AND group_id = "{group_id}"'.format(isNotified=1, group_id=1)).fetchall()]
    users_second = [i[0] for i in cur.execute('SELECT tg_id FROM users WHERE isNotified = "{isNotified}" AND group_id = "{group_id}"'.format(isNotified=1, group_id=2)).fetchall()]
    for user in users_first:
        if datetime.now().weekday() == 0:
            await bot.send_message(chat_id=user, text=msg_10t_1.monday, parse_mode='html')
        if datetime.now().weekday() == 1:
            await bot.send_message(chat_id=user, text=msg_10t_1.tuesday_first, parse_mode='html')
        if datetime.now().weekday() == 2:
            await bot.send_message(chat_id=user, text=msg_10t_1.wednesday_first, parse_mode='html')
        if datetime.now().weekday() == 3:
            await bot.send_message(chat_id=user, text=msg_10t_1.thursday_first, parse_mode='html')
        if datetime.now().weekday() == 4:
            await bot.send_message(chat_id=user, text=msg_10t_1.friday, parse_mode='html')
        if datetime.now().weekday() == 5:
            await bot.send_message(chat_id=user, text=msg_10t_1.saturday_first, parse_mode='html')
    for user_2 in users_second:
        if datetime.now().weekday() == 0:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.monday, parse_mode='html')
        if datetime.now().weekday() == 1:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.tuesday_second, parse_mode='html')
        if datetime.now().weekday() == 2:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.wednesday_second, parse_mode='html')
        if datetime.now().weekday() == 3:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.thursday_second, parse_mode='html')
        if datetime.now().weekday() == 4:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.friday, parse_mode='html')
        if datetime.now().weekday() == 5:
            await bot.send_message(chat_id=user_2, text=msg_10t_2.saturday_second, parse_mode='html')

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
scheduler.add_job(send_message_cron, 'cron', day_of_week='mon-sat', hour=7, minute=45)
scheduler.start()

@dp.message_handler(commands=['push'])
async def push(message: types.Message):
    if message.chat.id in admin_id:
        await bot.send_message(chat_id=message.chat.id, text='Напиши сообщение: ')
        await Form.my_message.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text='У вас нет доступа')

@dp.message_handler(state=Form.my_message)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['my_message'] = message.text
    await Form.next()
    await check_message(message)

async def check_message(message: types.Message):
    users = [row[0] for row in cur.execute('SELECT tg_id FROM users').fetchall()]
    for user in users:
        await bot.send_message(chat_id=user, text=message.text, parse_mode='html')

async def cmd_start_db(id: int, username: str):
    user = cur.execute('SELECT * FROM users WHERE tg_id == {key}'.format(key=id)).fetchone()
    username_name = cur.execute('SELECT * FROM users WHERE username == "{key}"'.format(key=username))
    if not user and username_name:
        cur.execute('''INSERT INTO users (tg_id, username) VALUES ("{key}", "{username}")'''.format(key=id, username=username))
        print(f'Пользователь {username} добавлен в базу данных!')
        db.commit()

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
        await cmd_start_db(message.from_user.id, f'@{message.from_user.username}')
        await select_class(message)

async def select_class(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Привет ты запустил бота! Теперь напиши свой класс: ")
    await Class_id.wait_for_class.set()

class Class_id(StatesGroup):
    wait_for_class = State()

@dp.message_handler(state=Class_id.wait_for_class)
async def proccess_select_class(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['wait_for_class'] = message.text
    await Class_id.next()
    await complete_class(message)

async def set_class(id: int, class_id: str):
    cur.execute('UPDATE users SET class_id = "{class_name}" WHERE tg_id = "{id}"'.format(class_name=class_id, id=id))

async def complete_class(message: types.Message):
    classes = ['10Т']
    if (isinstance(message.text, str) and 2 <= len(message.text) <= 3 and message.text.upper() in classes):
        await set_class(message.from_user.id, message.text.upper())
        await bot.send_message(chat_id=message.from_user.id, text=f'Успешно! Ваш класс: <b>{message.text}</b>', parse_mode='html')
        await group_selection(message)
    else:
        await bot.send_message(chat_id=message.chat.id, text='Ошибка! Введите корректный класс: ')
        await Class_id.wait_for_class.set()

async def group_selection(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    first_group = types.InlineKeyboardButton('1', callback_data='first_group')
    second_group = types.InlineKeyboardButton('2', callback_data='second_group')
    markup.add(first_group, second_group)
    await bot.send_message(chat_id=message.from_user.id, text='Вы вошли в систему групп!\nВыберите свою группу для продолжения', reply_markup=markup)

async def change_group_start(message):
    markup = types.InlineKeyboardMarkup()
    first_group = types.InlineKeyboardButton('1', callback_data='first_group')
    second_group = types.InlineKeyboardButton('2', callback_data='second_group')
    markup.add(first_group, second_group)
    await bot.send_message(chat_id=message.from_user.id, text='Выбери свою группу', parse_mode='html', reply_markup=markup)

async def start_schedule_first(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(kb.tommorow, kb.today, kb.days, kb.full, kb.uchitelya, kb.my_class, kb.comm, kb.donate, kb.profile)
    await bot.send_message(chat_id=message.chat.id,
                           text='Хороош, теперь можешь пользоваться ботом! Твоя группа: <b>1</b>', reply_markup=markup,
                           parse_mode='html')

async def start_schedule_second(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(kb.tommorow, kb.today, kb.days, kb.full, kb.uchitelya, kb.my_class, kb.comm, kb.donate, kb.profile)
    await bot.send_message(chat_id=message.chat.id,
                           text='Хороош, теперь можешь пользоваться ботом! Твоя группа: <b>2</b>', reply_markup=markup,
                           parse_mode='html')
    
async def donate(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    donatee = types.InlineKeyboardButton('Отправить донат', url='https://www.tinkoff.ru/rm/nurislamov.amir8/cktHx65549')
    markup.add(donatee)
    await bot.send_message(chat_id=message.chat.id,
                           text='Если вам нравится работа бота и вы хотите поддержать разработчика материально, можете отправить донат по кнопке ниже :)'.format(
                               message.from_user), reply_markup=markup)


async def change_group(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    change = types.InlineKeyboardButton('Изменить', callback_data='change')
    markup.row(change)
    await bot.send_message(chat_id=message.chat.id, text='Хочешь изменить группу?', reply_markup=markup)


async def my_class(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=msg_10t_1.cheliki, parse_mode='html')


async def changes_in_schedule(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пока изменений в расписании не обнаружено.',
                           parse_mode='html')



@dp.message_handler(content_types=['text'])
async def func(message: types.Message):
    await send_msg_10t.messages_10t(message)



async def add_user_to_group(id, group):
    cur.execute('UPDATE users SET group_id = {group} WHERE tg_id = "{id}"'.format(id=id, group=group))
    db.commit()

@dp.callback_query_handler()
async def callback(call: types.CallbackQuery) -> None:
    if call.data == 'change_group':
        await change_group(call.message)
    elif call.data == 'change':
        await change_group_start(call.message)
    elif call.data == 'donate':
        await donate(call.message)
    elif call.data == 'my_class':
        await my_class(call.message)
    elif call.data == 'changes_in_schedule':
        await changes_in_schedule(call.message)
    elif call.data == 'monday_first':
        await call.message.reply(msg_10t_1.monday, parse_mode='html')
    elif call.data == 'monday_second':
        await call.message.reply(msg_10t_2.monday, parse_mode='html')
    elif call.data == 'tuesday_first':
        await call.message.reply(msg_10t_1.tuesday_first, parse_mode='html')
    elif call.data == 'tuesday_second':
        await call.message.reply(msg_10t_2.tuesday_second, parse_mode='html')
    elif call.data == 'wednesday_first':
        await call.message.reply(msg_10t_1.wednesday_first, parse_mode='html')
    elif call.data == 'wednesday_second':
        await call.message.reply(msg_10t_2.wednesday_second, parse_mode='html')
    elif call.data == 'thursday_first':
        await call.message.reply(msg_10t_1.thursday_first, parse_mode='html')
    elif call.data == 'thursday_second':
        await call.message.reply(msg_10t_2.thursday_second, parse_mode='html')
    elif call.data == 'friday_first':
        await call.message.reply(msg_10t_1.friday, parse_mode='html')
    elif call.data == 'friday_second':
        await call.message.reply(msg_10t_2.friday, parse_mode='html')
    elif call.data == 'saturday_first':
        await call.message.reply(msg_10t_1.saturday_first, parse_mode='html')
    elif call.data == 'saturday_second':
        await call.message.reply(msg_10t_2.saturday_second, parse_mode='html')

    elif call.data == 'notify':
          markup = types.InlineKeyboardMarkup()
          on = types.InlineKeyboardButton('🔔 Включить оповещения', callback_data='on_notifications')
          off = types.InlineKeyboardButton('🔕 Выключить оповещения', callback_data='off_notifications')
          markup.add(on)
          markup.add(off)
          if call.from_user.id == call.message.chat.id:
              await bot.send_message(chat_id=call.message.chat.id,
                                 text='Чтобы включить или выключить оповещения от бота, нажмите на кнопки ниже.',
                                 reply_markup=markup)
          else:
              await bot.send_message(chat_id=call.message.chat.id, text="Данная функция работает только в личных сообщениях!")
    elif call.data == 'on_notifications':
        await notify_db(call.from_user.id, 1)
        await on_notify(call.message)
    elif call.data == 'off_notifications':
        await notify_db(call.from_user.id, 0)
        await off_notify(call.message)

    elif call.data == 'first_group':
        await add_user_to_group(call.from_user.id, 1)
        await start_schedule_first(call.message)
    elif call.data == 'second_group':
        await add_user_to_group(call.from_user.id, 2)
        await start_schedule_second(call.message)
    elif call.data == 'new_first_group' or call.data == 'new_second_group':
        await notifications(call.message)
keep_alive()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)