from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard = True).add(
    KeyboardButton('На завтра', callback_data='tommorow'),
    KeyboardButton('На сегодня', callback_data='today'),
    KeyboardButton('По дням', callback_data='days'),
    KeyboardButton('Полностью', callback_data='full'),
    KeyboardButton('Профиль', callback_data='profile'),
    KeyboardButton('Учителя', callback_data='uchitelya'),
    KeyboardButton('Мой класс', callback_data='my_class'),
    KeyboardButton('Обратная связь', callback_data='comm'),
    KeyboardButton('Донат', callback_data='donate'),
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

change_group = InlineKeyboardButton('Моя группа', callback_data='change_group')
donate = InlineKeyboardButton('Поддержать проект', callback_data='donate')
my_class = InlineKeyboardButton('Мой класс', callback_data='my_class')
changes_in_schedule = InlineKeyboardButton('Изменения в расписании', callback_data='changes_in_schedule')
notify = InlineKeyboardButton('Оповещения', callback_data='notify')
unregister = InlineKeyboardButton('Сбросить регистрацию', callback_data='unregister')