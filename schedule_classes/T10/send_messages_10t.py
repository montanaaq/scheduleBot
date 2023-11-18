from aiogram import types

import main
import schedule_classes.T10.messages_10t_1 as msg_10t_1
import schedule_classes.T10.messages_10t_2 as msg_10t_2
from datetime import datetime
import keyboards.keyboards as kb

async def messages_10t(message: types.Message):
        group_id = main.cur.execute('SELECT group_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=message.from_user.id)).fetchone()[0]
        class_id = main.cur.execute('SELECT class_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=message.from_user.id)).fetchone()[0]

        if (message.text == 'Мой класс' and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.cheliki, parse_mode='html')
        if (message.text == 'Учителя' and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.uchitelya, parse_mode='html')

        if (message.text == 'По дням' and group_id == 1 and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text='Здесь вы можете выбрать расписание по дням',
                                reply_markup=kb.days_first)
        if (message.text == 'По дням' and group_id == 2 and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text='Здесь вы можете выбрать расписание по дням',
                                reply_markup=kb.days_second)
            
        if (message.text == 'Полностью' and group_id == 1 and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.full_schedule_first, parse_mode='html')

        if (message.text == 'Полностью' and group_id == 2 and class_id == '10Т'):
            await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.full_schedule_second, parse_mode='html')

        if (message.text == 'На завтра'  and group_id == 1 and class_id == '10Т'):
            if (datetime.now().weekday() + 1 == 0):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.monday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 1):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.tuesday_first, parse_mode='html')
            if (datetime.now().weekday() + 1 == 2):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.wednesday_first, parse_mode='html')
            if (datetime.now().weekday() + 1 == 3):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.thursday_first, parse_mode='html')
            if (datetime.now().weekday() + 1 == 4):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.friday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 5):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.saturday_first, parse_mode='html')
            if (datetime.now().weekday() + 1 == 7):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.monday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 6):
                await main.bot.send_message(chat_id=message.from_user.id, text='Завтра выходной!')

        if (message.text == 'На завтра' and group_id == 2 and class_id == '10Т'):
            if (datetime.now().weekday() + 1 == 0):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.monday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 1):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.tuesday_second, parse_mode='html')
            if (datetime.now().weekday() + 1 == 2):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.wednesday_second, parse_mode='html')
            if (datetime.now().weekday() + 1 == 3):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.thursday_second, parse_mode='html')
            if (datetime.now().weekday() + 1 == 4):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.friday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 5):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.saturday_second, parse_mode='html')
            if (datetime.now().weekday() + 1 == 7):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.monday, parse_mode='html')
            if (datetime.now().weekday() + 1 == 6):
                await main.bot.send_message(chat_id=message.from_user.id, text='Завтра выходной!')

        if (message.text == 'На сегодня' and group_id == 1 and class_id == '10Т'):
            if (datetime.now().weekday() == 0):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.monday, parse_mode='html')
            if (datetime.now().weekday() == 1):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.tuesday_first, parse_mode='html')
            if (datetime.now().weekday() == 2):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.wednesday_first, parse_mode='html')
            if (datetime.now().weekday() == 3):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.thursday_first, parse_mode='html')
            if (datetime.now().weekday() == 4):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.friday, parse_mode='html')
            if (datetime.now().weekday() == 5):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_1.saturday_first, parse_mode='html')
            if (datetime.now().weekday() == 6):
                await main.bot.send_message(chat_id=message.from_user.id, text='Сегодня выходной!')

        if (message.text == 'На сегодня' and group_id == 2 and class_id == '10Т'):
            if (datetime.now().weekday() == 0):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.monday, parse_mode='html')
            if (datetime.now().weekday() == 1):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.tuesday_second, parse_mode='html')
            if (datetime.now().weekday() == 2):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.wednesday_second, parse_mode='html')
            if (datetime.now().weekday() == 3):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.thursday_second, parse_mode='html')
            if (datetime.now().weekday() == 4):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.friday, parse_mode='html')
            if (datetime.now().weekday() == 5):
                await main.bot.send_message(chat_id=message.from_user.id, text=msg_10t_2.saturday_second, parse_mode='html')
            if (datetime.now().weekday() == 6):
                await main.bot.send_message(chat_id=message.from_user.id, text='Сегодня выходной!')

        if (message.text == 'Донат' and class_id == '10Т'):
            markup = types.InlineKeyboardMarkup()
            donatee = types.InlineKeyboardButton('Отправить донат',
                                                url='https://www.tinkoff.ru/rm/nurislamov.amir8/cktHx65549')
            markup.add(donatee)
            await main.bot.send_message(chat_id=message.from_user.id,
                                text='Если вам нравится работа бота и вы хотите поддержать разработчика материально, можете отправить донат по кнопке ниже :)', reply_markup=markup)
        if (message.text == 'Обратная связь' and class_id == '10Т'):
            markup = types.InlineKeyboardMarkup()
            razrab = types.InlineKeyboardButton("Продолжить", url='https://t.me/montaanaq')
            markup.add(razrab)
            await main.bot.send_message(chat_id=message.from_user.id,
                                text='Писать только по работе бота, если нашли баг, без лишнего и спама. Чтобы связаться с разработчиком нажмите на кнопку ниже', reply_markup=markup)
            
        if (message.text == 'Профиль' and class_id == '10Т'):
            markup = types.InlineKeyboardMarkup(resize_keyboard = True)
            markup.row(kb.change_group)
            markup.row(kb.donate)
            markup.row(kb.my_class)
            markup.row(kb.notify)
            markup.row(kb.changes_in_schedule)
            markup.row(kb.unregister)
            await main.bot.send_message(chat_id=message.from_user.id, text='Профиль', reply_markup=markup)