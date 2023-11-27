from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard = True, row_width=2)
main.row(KeyboardButton('На завтра', callback_data='tommorow'))
main.row(
    KeyboardButton('На сегодня', callback_data='today'),
    KeyboardButton('По дням', callback_data='days'),
    KeyboardButton('Полностью', callback_data='full')
    )
main.row(
    KeyboardButton('Профиль', callback_data='profile'),
    KeyboardButton('Учителя', callback_data='uchitelya'),
    KeyboardButton('Мой класс', callback_data='my_class')
    )
main.row(
    KeyboardButton('Обратная связь', callback_data='comm'),
    KeyboardButton('Донат', callback_data='donate')
    )

days_first = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Понедельник', callback_data='monday_first'),
    InlineKeyboardButton('Вторник', callback_data='tuesday_first'),
    InlineKeyboardButton('Среда', callback_data='wednesday_first'),
    InlineKeyboardButton('Четверг', callback_data='thursday_first'),
    InlineKeyboardButton('Пятница', callback_data='friday_first'),
    InlineKeyboardButton('Суббота', callback_data='saturday_first'),
)
days_second = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Понедельник', callback_data='monday_second'),
    InlineKeyboardButton('Вторник', callback_data='tuesday_second'),
    InlineKeyboardButton('Среда', callback_data='wednesday_second'),
    InlineKeyboardButton('Четверг', callback_data='thursday_second'),
    InlineKeyboardButton('Пятница', callback_data='friday_second'),
    InlineKeyboardButton('Суббота', callback_data='saturday_second'),
)

change_group = InlineKeyboardButton('Изменить группу', callback_data='change_group')
donate = InlineKeyboardButton('Поддержать проект', callback_data='donate')
my_class = InlineKeyboardButton('Мой класс', callback_data='my_class')
changes_in_schedule = InlineKeyboardButton('Изменения в расписании', callback_data='changes_in_schedule')
notify = InlineKeyboardButton('Оповещения', callback_data='notify')
unregister = InlineKeyboardButton('Сбросить регистрацию', callback_data='unregister')

on = InlineKeyboardButton('🔔 Включить оповещения', callback_data='on_notifications')
off = InlineKeyboardButton('🔕 Выключить оповещения', callback_data='off_notifications')

notify_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
notify_keyboard.add(on)
notify_keyboard.add(off)

register = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).row(
    InlineKeyboardButton('Зарегистрироваться', callback_data='register')
)

start_edit = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).row(
    InlineKeyboardButton('Начать редактирование', callback_data='start_editing')
)

classes = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    InlineKeyboardButton('10Т', callback_data='edit_10t')
)

weekdays = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    InlineKeyboardButton('Понедельник', callback_data='edit_monday'),
    InlineKeyboardButton('Вторник', callback_data='edit_tuesday'),
    InlineKeyboardButton('Среда', callback_data='edit_wednesday'),
    InlineKeyboardButton('Четверг', callback_data='edit_thursday'),
    InlineKeyboardButton('Пятница', callback_data='edit_friday'),
    InlineKeyboardButton('Суббота', callback_data='edit_saturday'),
)

select_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    InlineKeyboardButton('1', callback_data='edit_first_group'),
    InlineKeyboardButton('2', callback_data='edit_second_group'),
)