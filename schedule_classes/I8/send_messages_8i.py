from aiogram import types

import main
import schedule_classes.I8.messages_8i_1 as msg_8i_1
import schedule_classes.I8.messages_8i_2 as msg_8i_2
from datetime import datetime
import keyboards.keyboards as kb

async def messages_8i(message: types.Message):
        users = [row[0] for row in main.cur.execute('SELECT tg_id FROM users WHERE tg_id="{id}" AND class_id = 0'.format(id=message.from_user.id)).fetchall()]
        users_id = [row[0] for row in main.cur.execute('SELECT tg_id FROM users').fetchall()]
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
        if (message.text in formatted_messages and not message.from_user.id in users_id):
          await main.bot.send_message(chat_id=message.from_user.id, text='Мы не нашли вас в базе данных, попробуйте /start и повторите попытку!')
        else:
          if message.from_user.id in users:
            await main.bot.send_message(chat_id=message.from_user.id, text='Мы не нашли вас в базе данных, попробуйте /start и повторите попытку!')
          else:
            group_id = main.cur.execute('SELECT group_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=message.from_user.id)).fetchone()[0]
            class_id = main.cur.execute('SELECT class_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=message.from_user.id)).fetchone()[0]
    
            if (message.text == 'Мой класс' and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text='Данная функций не работает. Отправьте данные о классе @montaanaq', parse_mode='html')
            if (message.text == 'Учителя' and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text='Данная функций не работает. Отправьте данные о учителях @montaanaq', parse_mode='html')
    
            if (message.text == 'По дням' and group_id == 1 and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text='Здесь вы можете выбрать расписание по дням',
                                    reply_markup=kb.days_first)
            if (message.text == 'По дням' and group_id == 2 and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text='Здесь вы можете выбрать расписание по дням',
                                    reply_markup=kb.days_second)
                
            if (message.text == 'Полностью' and group_id == 1 and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('full')), parse_mode='html')
    
            if (message.text == 'Полностью' and group_id == 2 and class_id == '8И'):
                await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('full')), parse_mode='html')
    
            if (message.text == 'На завтра'  and group_id == 1 and class_id == '8И'):
                if (datetime.now().weekday() + 1 == 0):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 1):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('tuesday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 2):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('wednesday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 3):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('thursday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 4):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('friday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 5):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('saturday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 7):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 6):
                    await main.bot.send_message(chat_id=message.from_user.id, text='Завтра выходной 😁')
    
            if (message.text == 'На завтра' and group_id == 2 and class_id == '8И'):
                if (datetime.now().weekday() + 1 == 0):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 1):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('tuesday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 2):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('wednesday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 3):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('thursday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 4):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('friday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 5):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('saturday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 7):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() + 1 == 6):
                    await main.bot.send_message(chat_id=message.from_user.id, text='Завтра выходной 😁')
    
            if (message.text == 'На сегодня' and group_id == 1 and class_id == '8И'):
                if (datetime.now().weekday() == 0):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() == 1):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('tuesday')), parse_mode='html')
                if (datetime.now().weekday() == 2):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('wednesday')), parse_mode='html')
                if (datetime.now().weekday() == 3):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('thursday')), parse_mode='html')
                if (datetime.now().weekday() == 4):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('friday')), parse_mode='html')
                if (datetime.now().weekday() == 5):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_1.return_schedule('saturday')), parse_mode='html')
                if (datetime.now().weekday() == 6):
                    await main.bot.send_message(chat_id=message.from_user.id, text='Сегодня выходной!')
    
            if (message.text == 'На сегодня' and group_id == 2 and class_id == '8И'):
                if (datetime.now().weekday() == 0):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('monday')), parse_mode='html')
                if (datetime.now().weekday() == 1):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('tuesday')), parse_mode='html')
                if (datetime.now().weekday() == 2):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('wednesday')), parse_mode='html')
                if (datetime.now().weekday() == 3):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('thursday')), parse_mode='html')
                if (datetime.now().weekday() == 4):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('friday')), parse_mode='html')
                if (datetime.now().weekday() == 5):
                    await main.bot.send_message(chat_id=message.from_user.id, text=(await msg_8i_2.return_schedule('saturday')), parse_mode='html')
                if (datetime.now().weekday() == 6):
                    await main.bot.send_message(chat_id=message.from_user.id, text='Сегодня выходной!')
    
            if (message.text == 'Донат' and class_id == '8И'):
                markup = types.InlineKeyboardMarkup()
                donatee = types.InlineKeyboardButton('Отправить донат',
                                                    url='https://www.tinkoff.ru/rm/nurislamov.amir8/cktHx65549')
                markup.add(donatee)
                await main.bot.send_message(chat_id=message.from_user.id,
                                    text='Если вам нравится работа бота и вы хотите поддержать разработчика материально, можете отправить донат по кнопке ниже :)', reply_markup=markup)
            if (message.text == 'Обратная связь' and class_id == '8И'):
                markup = types.InlineKeyboardMarkup()
                razrab = types.InlineKeyboardButton("Продолжить", url='https://t.me/montaanaq')
                markup.add(razrab)
                await main.bot.send_message(chat_id=message.from_user.id,
                                    text='Писать только по работе бота, если нашли баг, без лишнего и спама. Чтобы связаться с разработчиком нажмите на кнопку ниже', reply_markup=markup)
                
            if (message.text == 'Профиль' and class_id == '8И'):
                markup = types.InlineKeyboardMarkup(resize_keyboard = True)
                markup.row(kb.change_group)
                markup.row(kb.donate)
                markup.row(kb.my_class)
                markup.row(kb.notify)
                markup.row(kb.changes_in_schedule)
                markup.row(kb.unregister)
                await main.bot.send_message(chat_id=message.from_user.id, text='Профиль', reply_markup=markup)