from aiogram import types
import main
import schedule_classes.T10.messages_10t_1 as msg_10t_1
import schedule_classes.T10.messages_10t_2 as msg_10t_2
import keyboards.keyboards as kb

async def callbacks(call: types.CallbackQuery):
    class_id = main.cur.execute('SELECT class_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=call.from_user.id)).fetchone()[0]
    if call.data == 'monday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('monday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'monday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('monday')), parse_mode='html', reply_markup=kb.days_second)
    elif call.data == 'tuesday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('tuesday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'tuesday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('tuesday')), parse_mode='html', reply_markup=kb.days_second)
    elif call.data == 'wednesday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('wednesday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'wednesday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('wednesday')), parse_mode='html', reply_markup=kb.days_second)
    elif call.data == 'thursday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('thursday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'thursday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('thursday')), parse_mode='html', reply_markup=kb.days_second)
    elif call.data == 'friday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('friday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'friday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('friday')), parse_mode='html', reply_markup=kb.days_second)
    elif call.data == 'saturday_first' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_1.return_schedule('saturday')), parse_mode='html', reply_markup=kb.days_first)
    elif call.data == 'saturday_second' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=(await msg_10t_2.return_schedule('saturday')), parse_mode='html', reply_markup=kb.days_second)

async def profile(call: types.CallbackQuery):
    class_id = main.cur.execute('SELECT class_id FROM users WHERE tg_id ="{user_id}"'.format(user_id=call.from_user.id)).fetchone()[0]
    if call.data == 'change_group' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.change_group(call.message)
    elif call.data == 'change' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.change_group_start(call.message)
    elif call.data == 'donate' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.donate(call.message)
    elif call.data == 'my_class' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.bot.send_message(chat_id=call.message.chat.id, text=msg_10t_1.cheliki, parse_mode='html')
    elif call.data == 'changes_in_schedule' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.changes_in_schedule(call.message)
    elif call.data == 'unregister' and class_id == '10Т':
        await main.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await main.proccess_unregister(call.from_user.id)
        await main.bot.send_message(chat_id=call.message.chat.id, text='<b>Вы успешно сбросили регистрацию!</b>\n\n<i>/start</i> - для начала работы бота', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())