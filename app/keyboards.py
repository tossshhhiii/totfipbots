from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание'), KeyboardButton(text='Изменения')],
    [KeyboardButton(text='Расписание звонков')]
],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите пункт меню.')


back_schedule = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_schedule')],
])

back_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_main')],
])


inline_schedule = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 курс', callback_data='one_course')],
    [InlineKeyboardButton(text='2 курс', callback_data='two_course')],
    [InlineKeyboardButton(text='3 курс', callback_data='free_course')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])
