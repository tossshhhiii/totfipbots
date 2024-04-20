from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.methods import DeleteMessages


import app.keyboards as kb
# import app.database.requets as rq

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # await rq.set_user(message.from_user.id)
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать!', reply_markup=kb.main)


#ijdfipshdpiufhishdiapudipuafipuhsdgipuhsvipusfahgihdafg[fdo[gi[dariuhgdaipfgipdfhipudhgfpiuhdfpiuhdsgipuh]]]
@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply(message.photo[-1].file_id)


#!!!!!!!!!!!!!!!
@router.message(Command('problem'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?')
    await message.answer(f'Ваш ID: {message.from_user.id}')

#main

@router.message(F.text == 'Расписание')
async def schedule(message: Message):
    await message.answer(f'Выберите подходящий вам курс.', reply_markup=kb.inline_schedule)
    await message.bot.delete_message(message.chat.id, message.message_id)

@router.message(F.text == 'Расписание звонков')
async def schedule(message: Message):
    await message.answer_photo('https://xn--h1alejbm.xn--p1ai/files/docs/local-acts/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%BE%D0%B2%202023.jpg', reply_markup=kb.back_main)
    await message.bot.delete_message(message.chat.id, message.message_id)

@router.message(F.text == 'Изменения')
async def changes(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBxWYg5o5O9oE_Jxt30jIKsdEDOwcRAAJf1jEbA7EJSW1kLt4u-jzYAQADAgADeQADNAQ', reply_markup=kb.back_main)


#inline_schedule
    
@router.callback_query(F.data == 'one_course')
async def one_course(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer_document('https://xn--h1alejbm.xn--p1ai/files/docs/local-acts/raspisanie/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%201%20%D0%BA%D1%83%D1%80%D1%81%D1%8B%2015.04-27.04.2024.pdf', reply_markup=kb.back_schedule)

@router.callback_query(F.data == 'two_course')
async def one_course(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer_document('https://xn--h1alejbm.xn--p1ai/files/docs/local-acts/raspisanie/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%202%20%D0%BA%D1%83%D1%80%D1%81%D1%8B%2015.04-27.04.2024.pdf', reply_markup=kb.back_schedule)


@router.callback_query(F.data == 'free_course')
async def one_course(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer_document('https://xn--h1alejbm.xn--p1ai/files/docs/local-acts/raspisanie/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%203%20%D0%BA%D1%83%D1%80%D1%81%D1%8B%2015.04-27.04.2024.pdf', reply_markup=kb.back_schedule)

#back 
    
@router.callback_query(F.data == 'back')
async def call_main_menu(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)



#back schedule 
@router.callback_query(F.data == 'back_schedule')
async def call_main_menu(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer(f'Выберите подходящий вам курс.', reply_markup=kb.inline_schedule)
    

#back main 
@router.callback_query(F.data == 'back_main')
async def call_main_menu(callback: CallbackQuery):
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    
    
    
   
    
