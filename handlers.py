from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from states.create_profile import FSMProfile
from utils.db_api import database
from loader import dp
from utils.db_api.database import User
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton,
                           CallbackQuery, LabeledPrice, PreCheckoutQuery)
from aiogram.utils.callback_data import CallbackData


db = database.DBCommands()



@dp.message_handler(commands=['profile'])
async def get_profile(message: types.Message):
    create_fake_profile = await db.fill_base()
    get_profile_item = await db.show_my_profile()
    print(get_profile_item)






# get_all_use = await db.get_data()
#     # print(get_all_use)
#     # for item in get_all_use:
#     #     await message.answer(item.photo_profile)








@dp.message_handler(commands=['start'])
async def register_user(message: types.Message):
    # fill_user = await db.fill_base()
    # get_user = await db.get_data()
    # print(get_user)
    # get_all_use = await db.get_data()
    # print(get_all_use)
    # for item in get_all_use:
    #     await message.answer(item.photo_profile)
    # user = types.User.get_current().
    # await message.answer(user)
    profile = await db.add_new_profile()
    languages_markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
            [
                InlineKeyboardButton(text="English", callback_data="lang_en"),
                InlineKeyboardButton(text="Україньска", callback_data="lang_uk"),
            ]
        ]
    )
    await message.answer("Выберите ваш язык", reply_markup=languages_markup)

@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    await db.get_language(lang)
    await call.message.answer("Язык установлен")
    await call.answer()



async def msg_load_name(message: types.Message):
    await message.answer("Введите ваше имя")
    await FSMProfile.name.set()

async def load_name(message: types.Message, state:FSMContext):
    name = message.text
    user_prof = User()
    user_prof.username = name
    await message.answer("Загрузите ваше фото")
    await FSMProfile.photo.set()
    await state.update_data(user_prof=user_prof)

#загрузка главных фото профиля и запрос имени
# @dp.message_handler(content_types="photo", state=FSMProfile.photo)
async def load_profile_photo(message: types.Message, state: FSMContext):
        photo = message.photo[-1].file_id
        data = await state.get_data()
        user_prof: User = data.get("user_prof")
        user_prof.photo_profile = photo
        await message.answer("Ваш возвраст")




async def load_age(message: types.Message, state: FSMContext):

    await user_prof.create()
    await state.reset_state()





















# # захват ответа возраста и обработка возраста пользователя
# async def load_age(message: types.Message, state:FSMContext):
#     async with state.proxy() as data:
#         data["age"] = message.text
#         # await message.answer("Выберите ваш пол", reply_markup=metabolism_gender_markup)
#         await FSMProfile.next()
#         await message.answer("Введите ваши хобби")
#захват пола польователя и запрос хобби
# @dp.callback_query_handler(gender_callback.filter(), state=FSMProfile.gender)
# async def load_gender(call: CallbackQuery, callback_data: dict, state: FSMContext, gender_item=None):
#     async with state.proxy() as data:
#         print(callback_data.get('description'))
#         data['gender'] = callback_data.get('description')
#         print(data['gender'])
#         await FSMProfile.next()
#         await call.message.answer("Введите ваши хобби")


# захват ответа хобби и обработка хобби пользователя
# async def load_hobby(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["hobby"] = message.text
#         await message.answer("Ваша анкета успешно загружена!")
#         await message.answer(data)
#         await message.answer(data.values())
#         data_prof = await state.get_data()
#         print(data_prof)
#         print(type(data_prof))
#         # fillthebase = data.values()
#         # print(type(fillthebase))
#         # print(fillthebase[0])
#         # print(fillthebase[1])
#         # print(fillthebase[2])
#         # print(fillthebase[3])
#         # await sql_add_profile(state)
#         await state.finish()






#собираем хендлеры регистрации нового пользователя
def register_handlers_profile_reg(dp : Dispatcher):
    dp.register_message_handler(msg_load_name, commands="edit", state=None)
    dp.register_message_handler(load_name, state=FSMProfile.name)
    dp.register_message_handler(load_profile_photo, content_types="photo", state=FSMProfile.photo)
    dp.register_message_handler(load_age, state=FSMProfile.age)
    # dp.register_callback_query_handler(load_gender, state=FSMProfile.gender)
    # dp.register_message_handler(load_hobby, state=FSMProfile.hobby)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(register_user, commands=["start"])