from aiogram import types

tommorow = types.KeyboardButton('На завтра')
today = types.KeyboardButton('На сегодня')
days = types.KeyboardButton('По дням')
comm = types.KeyboardButton('Обратная связь')
donate = types.KeyboardButton('Донат')
full = types.KeyboardButton('Полностью')
uchitelya = types.KeyboardButton('Учителя')
my_class = types.KeyboardButton('Мой класс')
profile = types.KeyboardButton('Профиль')

days_first = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton('Понедельник', callback_data='monday_first'),
    types.InlineKeyboardButton('Вторник', callback_data='tuesday_first'),
    types.InlineKeyboardButton('Среда', callback_data='wednesday_first'),
    types.InlineKeyboardButton('Четверг', callback_data='thursday_first'),
    types.InlineKeyboardButton('Пятница', callback_data='friday_first'),
    types.InlineKeyboardButton('Суббота', callback_data='saturday_first'),
)
days_second = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton('Понедельник', callback_data='monday_second'),
    types.InlineKeyboardButton('Вторник', callback_data='tuesday_second'),
    types.InlineKeyboardButton('Среда', callback_data='wednesday_second'),
    types.InlineKeyboardButton('Четверг', callback_data='thursday_second'),
    types.InlineKeyboardButton('Пятница', callback_data='friday_second'),
    types.InlineKeyboardButton('Суббота', callback_data='saturday_second'),
)

change_group = types.InlineKeyboardButton('Моя группа', callback_data='change_group')
donate = types.InlineKeyboardButton('Поддержать проект', callback_data='donate')
my_class = types.InlineKeyboardButton('Мой класс', callback_data='my_class')
changes_in_schedule = types.InlineKeyboardButton('Изменения в расписании', callback_data='changes_in_schedule')
notify = types.InlineKeyboardButton('Оповещения', callback_data='notify')