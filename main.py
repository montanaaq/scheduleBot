#            .oooooo..o   .oooooo.   ooooo   ooooo oooooooooooo oooooooooo.   ooooo     ooo ooooo        oooooooooooo      oooooooooo.    .oooooo.   ooooooooooooo 
#            d8P'    `Y8  d8P'  `Y8b  `888'   `888' `888'     `8 `888'   `Y8b  `888'     `8' `888'        `888'     `8      `888'   `Y8b  d8P'  `Y8b  8'   888   `8 
#            Y88bo.      888           888     888   888          888      888  888       8   888          888               888     888 888      888      888      
#            `"Y8888o.  888           888ooooo888   888oooo8     888      888  888       8   888          888oooo8          888oooo888' 888      888      888      
#                `"Y88b 888           888     888   888    "     888      888  888       8   888          888    "          888    `88b 888      888      888      
#            oo     .d8P `88b    ooo   888     888   888       o  888     d88'  `88.    .8'   888       o  888       o       888    .88P `88b    d88'      888      
#            8""88888P'   `Y8bood8P'  o888o   o888o o888ooooood8 o888bood8P'      `YbodP'    o888ooooood8 o888ooooood8      o888bood8P'   `Y8bood8P'      o888o                                                                                                                                  

#                                                         Imports
from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import time
from datetime import datetime
from config import BOT_TOKEN, admin_id

import schedule_classes.T10.messages_10t_1 as msg_10t_1
import schedule_classes.T10.messages_10t_2 as msg_10t_2
import schedule_classes.T10.send_messages_10t as send_msg_10t
import schedule_classes.T10.callbacks as callbacks_10t

import schedule_classes.I8.messages_8i_1 as msg_8i_1
import schedule_classes.I8.messages_8i_2 as msg_8i_2
import schedule_classes.I8.send_messages_8i as send_msg_8i
import schedule_classes.I8.callbacks as callbacks_8i

import keyboards.keyboards as kb
import database_start as db_start

import sqlite3 as sql

# from background import keep_alive

db = sql.connect('database/database.db')
cur = db.cursor()

db_sub = sql.connect('database/subjects.db')
cur_sub = db_sub.cursor()

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

async def main():
    await send_msg_10t.send_message_cron()

async def on_startup(_):
    await db_start.main_db_start()

    # await db_start.t10_db_start_1()
    # await db_start.t10_db_start_2()
    # await msg_8i_1.i8_db_start_1()
    # await msg_8i_2.i8_db_start_2()

    await db_start.create_subjects_1()
    await db_start.create_subjects_2()
    await msg_8i_1.create_subjects_1()
    await msg_8i_2.create_subjects_2()
    print('Database started!')
    print('Bot started!')

class Form(StatesGroup):
    my_message = State()
    check_class = State()

# ---------------------------------------------------- Notifications ---------------------------------------------------
# @dp.message_handler(commands=['webapp'])
# async def webapp(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     webapp = types.WebAppInfo("https://schedule-bot.netlify.app")
#     web = types.KeyboardButton('🔗 Расписание', web_app=webapp)
#     markup.add(web)
#     await bot.send_message(chat_id=message.chat.id, text='Привет! Нажми кнопку ниже, чтобы открыть сайт', reply_markup=markup)

@dp.message_handler(commands=['unregister'])
async def unregister(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Чтобы сбросить регистрацию, нажми на кнопку ниже', reply_markup=kb.unregister_markup)

@dp.message_handler(commands=['notify'])
async def notifications(message: types.Message):
    users = [row[0] for row in cur.execute('SELECT tg_id FROM users WHERE class_id = 0').fetchall()]
    users_id = [row[0] for row in cur.execute('SELECT tg_id FROM users').fetchall()]
    if message.from_user.id in users_id:
      if not message.from_user.id in users:
          markup = types.InlineKeyboardMarkup()
          markup.add(kb.on)
          markup.add(kb.off)
          if message.from_user.id == message.chat.id:
              await bot.send_message(chat_id=message.chat.id,
                              text='Чтобы включить или выключить оповещения от бота, нажмите на кнопки ниже.',
                              reply_markup=markup)
          else:
              await bot.send_message(chat_id=message.chat.id, text="Данная функция работает только в личных сообщениях!")
      else:
          await bot.send_message(chat_id=message.from_user.id, text='Вы не можете включить уведомления без регистрации! /start')
    else:
      await bot.send_message(chat_id=message.from_user.id, text='Вы не можете включить уведомления без регистрации! /start')

async def notify_db(id: int, isNotified: int):
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

async def start_scheduler(class_id):
    if class_id == '10Т':
        scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        scheduler.add_job(send_msg_10t.send_message_cron, 'cron', day_of_week='mon-sat', hour=7, minute=45)
        scheduler.start()
    if class_id == '8И':        
        scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        scheduler.add_job(send_msg_8i.send_message_cron, 'cron', day_of_week='mon-sat', hour=7, minute=45)
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
        user = cur.execute('SELECT tg_id FROM users WHERE tg_id = "{id}" AND class_id != 0'.format(id=message.from_user.id)).fetchone()
        if not user:
            await cmd_start_db(message.from_user.id, f'@{message.from_user.username}')
            await select_class(message)
        else:
            await bot.send_message(chat_id=message.chat.id, text='Ты уже зарегестрирован в базе данных!')

@dp.message_handler(commands=['edit'])
async def edit_panel(message: types.Message):
    if message.from_user.id in admin_id:
        await bot.send_message(chat_id=message.from_user.id, text=f'Привет <b>{message.from_user.username},</b> здесь ты можешь редактировать расписание всех классов', parse_mode='html', reply_markup=kb.start_edit)
    else:
        await bot.send_message(chat_id=message.from_user.id, text='У вас нет прав!')

async def edit_class(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Выбери класс для редактирования', reply_markup=kb.classes)

async def edit_classes(call: types.CallbackQuery):
    global choosen_class
    if call.data == 'edit_10t':
        choosen_class = '10Т'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await select_edit_group(call.message)

async def select_edit_group(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Выбери группы для которой нужно изменить расписание', reply_markup=kb.select_group)

async def select_edit_group_callback(call: types.CallbackQuery):
    global choosen_group
    if call.data == 'edit_first_group':
        choosen_group = 1
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await select_edit_weekday(call.message)
    if call.data == 'edit_second_group':
        choosen_group = 2
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await select_edit_weekday(call.message)
        
async def select_edit_weekday(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Выбери день недели, который вы хотите отредактировать', reply_markup=kb.weekdays)

async def select_weekday(call: types.CallbackQuery):
    global choosen_weekday
    if call.data == 'edit_monday':
        choosen_weekday = 'Понедельник'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)
    elif call.data == 'edit_tuesday':
        choosen_weekday = 'Вторник'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)
    elif call.data == 'edit_wednesday':
        choosen_weekday = 'Среда'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)
    elif call.data == 'edit_thursday':
        choosen_weekday = 'Четверг'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)
    elif call.data == 'edit_friday':
        choosen_weekday = 'Пятница'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)
    elif call.data == 'edit_saturday':
        choosen_weekday = 'Суббота'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await accept_data(call.message)

class AcceptData(StatesGroup):
    data = State()

async def accept_data(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Напишите как в примере\n\n<b>Номер урока, название предмета, кабинет</b>\n\nЗапятые обязательны', parse_mode='html')
    await AcceptData.data.set()

@dp.message_handler(state=AcceptData.data)
async def proccess_accept_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    await AcceptData.next()
    await check_data(message)

async def check_data(message: types.Message):
    global choosen_class
    global choosen_group
    global choosen_weekday

    sended_message = (message.text).split(', ')
    subjects = [
        'Математика',
        'Русс.яз',
        'Общество',
        'ОБЖ',
        'История',
        'Англ.яз',
        'Франц.яз',
        'Информатика',
        'Литер',
        'Эл.физика',
        'Физ-ра',
        'Геометрия',
        'Алгебра',
        'Вероятность',
        'Химия',
        'Физика',
        'Биология',
        'География',
        'Родн.яз',
        ]
    if len(sended_message) < 3:
        await bot.send_message(chat_id=message.from_user.id, text='Неверный формат данных! Попробуйте ещё раз')
        await AcceptData.data.set()
    else:
        number_of_lesson = sended_message[0]
        name_of_subject = sended_message[1]
        cabinet_name = sended_message[2]
        if len(sended_message) > 3 and not name_of_subject in subjects and 0 < number_of_lesson <= 9:
            await bot.send_message(chat_id=message.from_user.id, text='Неверный формат данных! Попробуйте ещё раз')
            await AcceptData.data.set()
        else:
            await bot.send_message(chat_id=message.from_user.id, text='Успешно!')
            await set_data(choosen_class, choosen_group, choosen_weekday, number_of_lesson, name_of_subject, cabinet_name)

async def set_data(class_name, group, title, subj_id, subject, cabine):
    if class_name == '10Т' and group == 1:
        cur_sub.execute('UPDATE subjects_10t_1 SET subjects = "{subject}" WHERE title = "{title}" AND subj_id = "{subj_id}"'.format(
            subject=subject, title=title, subj_id=subj_id
        ))
        cur_sub.execute('UPDATE subjects_10t_1 SET cabines = "{cabine}" WHERE title = "{title}" AND subj_id = "{subj_id}"'.format(
            cabine=cabine, title=title, subj_id=subj_id
        ))
        db_sub.commit()
    elif class_name == '10Т' and group == 2:
        cur_sub.execute('UPDATE subjects_10t_2 SET subjects = "{subject}" WHERE title = "{title}" AND subj_id = "{subj_id}"'.format(
            subject=subject, cabine=cabine, title=title, subj_id=subj_id
        ))
        cur_sub.execute('UPDATE subjects_10t_2 SET cabines = "{cabine}" WHERE title = "{title}" AND subj_id = "{subj_id}"'.format(
            cabine=cabine, title=title, subj_id=subj_id
        ))
        db_sub.commit()

async def select_class(message: types.Message):
    global class_id
    class_id = await bot.send_message(chat_id=message.chat.id, text="Привет ты запустил бота! Теперь напиши свой класс: ")
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
    global class_id
    classes = ['10Т', '8И']
    if (isinstance(message.text, str) and 2 <= len(message.text) <= 3 and message.text.upper() in classes):
        await set_class(message.from_user.id, message.text.upper())
        await bot.delete_message(chat_id=message.chat.id, message_id=class_id.message_id)
        await bot.send_message(chat_id=message.from_user.id, text=f'✅ Успешно! Ваш класс: <b>{message.text}</b>', parse_mode='html')
        time.sleep(1)
        await group_selection(message)
    else:
        await bot.send_message(chat_id=message.chat.id, text='Ошибка! Введите корректный класс: \nПример: 10Т')
        await Class_id.wait_for_class.set()

async def group_selection(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    first_group = types.InlineKeyboardButton('1', callback_data='first_group')
    second_group = types.InlineKeyboardButton('2', callback_data='second_group')
    markup.add(first_group, second_group)
    await bot.send_message(chat_id=message.from_user.id, text='Вы вошли в систему групп!\nВыберите свою группу для продолжения', reply_markup=markup)

async def change_group_start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    first_group = types.InlineKeyboardButton('1', callback_data='first_group')
    second_group = types.InlineKeyboardButton('2', callback_data='second_group')
    markup.add(first_group, second_group)
    await bot.send_message(chat_id=message.chat.id, text='Выбери свою группу', parse_mode='html', reply_markup=markup)

async def start_schedule_first(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Хороош, теперь можешь пользоваться ботом! Твоя группа: <b>1</b>', reply_markup=kb.main,
                           parse_mode='html')

async def start_schedule_second(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Хороош, теперь можешь пользоваться ботом! Твоя группа: <b>2</b>', reply_markup=kb.main,
                           parse_mode='html')

@dp.message_handler(commands=['donate'])
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

async def changes_in_schedule(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Пока изменений в расписании не обнаружено.',
                           parse_mode='html')
                                                            # content_types=['text'])
@dp.message_handler(content_types=['text'])
async def func(message: types.Message):
    class_id = cur.execute('SELECT class_id FROM users WHERE tg_id = "{id}"'.format(id=message.from_user.id)).fetchone()[0]
    users = [row[0] for row in cur.execute('SELECT tg_id FROM users WHERE class_id = 0').fetchall()]
    users_id = [row[0] for row in cur.execute('SELECT tg_id FROM users').fetchall()]
    formatted_messages = [
          'На завтра',
          'На сегодня',
          'Полностью',
          'По дням',
          'Профиль',
          'Донат',
          '/notify',
          'Обратная связь',
          'Учителя',
          'Мой класс',
        ]
    if class_id == '0':
        if (message.text in formatted_messages and not message.from_user.id in users_id or message.text in formatted_messages and message.from_user.id in users):
          await bot.send_message(chat_id=message.from_user.id, text='Мы не нашли вас в базе данных, попробуйте /start и повторите попытку!')
    if message.text not in formatted_messages:
            await bot.send_message(chat_id=message.chat.id, text='Я тебя не понимаю...')
    elif class_id == '8И':
        await send_msg_8i.messages_8i(message)
    elif class_id == '10Т':
        await send_msg_10t.messages_10t(message)
async def add_user_to_group(id: int, group: int):
    cur.execute('UPDATE users SET group_id = "{group}" WHERE tg_id = "{id}"'.format(id=id, group=int(group)))
    db.commit()

async def proccess_unregister(id: int):
    cur.execute('UPDATE users SET class_id = "" AND group_id = "0" WHERE tg_id = "{id}"'.format(id=id))
    db.commit()

                                                            # callbacks
@dp.callback_query_handler()
async def callback(call: types.CallbackQuery) -> None:
    # profile
    await callbacks_8i.profile(call)
    await callbacks_10t.profile(call)
    # days
    await callbacks_10t.callbacks(call)
    await callbacks_8i.callbacks(call)
    # notifications    

    if call.data == 'unreg':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await proccess_unregister(call.from_user.id)
        await bot.send_message(chat_id=call.message.chat.id, text='<b>Вы успешно сбросили регистрацию!</b>\n\n<i>/start</i> - для начала работы бота', parse_mode='html', reply_markup=types.ReplyKeyboardRemove())

    if call.data == 'register':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await start_command(call.message)

    elif call.data == 'notify':
          await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
          if call.from_user.id == call.message.chat.id:
              await bot.send_message(chat_id=call.message.chat.id,
                                 text='Чтобы включить или выключить оповещения от бота, нажмите на кнопки ниже.',
                                 reply_markup=kb.notify_keyboard)
          else:
              await bot.send_message(chat_id=call.message.chat.id, text="Данная функция работает только в личных сообщениях!")
    elif call.data == 'on_notifications':
        await notify_db(call.from_user.id, 1)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        class_id = cur.execute('SELECT class_id FROM users WHERE tg_id = "{id}"'.format(id=call.from_user.id)).fetchone()[0]
        await start_scheduler(class_id)
        await on_notify(call.message)
    elif call.data == 'off_notifications':
        await notify_db(call.from_user.id, 0)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await off_notify(call.message)

    # registration
    elif call.data == 'first_group':
        await add_user_to_group(call.from_user.id, 1)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await start_schedule_first(call.message)
    elif call.data == 'second_group':
        await add_user_to_group(call.from_user.id, 2)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await start_schedule_second(call.message)
    elif call.data == 'new_first_group' or call.data == 'new_second_group':
        await notifications(call.message)

    # edit
    elif call.data == 'start_editing':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await edit_class(call.message)
    await edit_classes(call)
    await select_edit_group_callback(call)
    await select_weekday(call)

# keep_alive()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)