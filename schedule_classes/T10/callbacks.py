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
