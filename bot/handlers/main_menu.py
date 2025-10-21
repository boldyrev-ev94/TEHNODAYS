from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import copy

from keyboards.main_menu import get_main_menu_kb, get_create_user, get_add_category_data
from model.User import User
from model.Category import Category


class Questionnaire(StatesGroup):
    user = User(0, "", "")
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()

# Класс состояний бота


class SearchUser(StatesGroup):
    question1 = State()


# storage = MemoryStorage()
router = Router()
list_user = []


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "ТЕХНОПРЕДКИ ОНЛАЙН",
        reply_markup=get_main_menu_kb()
    )


@router.message(Command("users"))
async def get_users(message: Message):
    for user in list_user:
        u = user.get_info()

        msg = f"""
        №_ {u['id']}
        {u['surname']} {u['name']}
        """
        await message.answer(msg)


@router.callback_query(F.data == "add_new_user")
async def add_new_user(callback: types.CallbackQuery, state: FSMContext):
    msg = f"""
Добавление нового участника
Введите фамилию: 
"""
    await callback.message.answer(msg)
    await state.set_state(Questionnaire.question1)


@router.message(Questionnaire.question1)
async def process_set_name_user(message: Message, state: FSMContext):
    try:
        Questionnaire.user.update("surname", message.text.lower().capitalize())
        await message.answer("Введите Имя")
        await state.set_state(Questionnaire.question2)
    except:
        await message.answer("Ошибка ввода.\n Введите Фамилию еще раз:")
        await state.set_state(Questionnaire.question1)


@router.message(Questionnaire.question2)
async def process_set_surname_user(message: Message, state: FSMContext):
    try:
        Questionnaire.user.update("name", message.text.lower().capitalize())
        await message.answer("Введите id")
        await state.set_state(Questionnaire.question3)
    except:
        await message.answer("Ошибка ввода.\n Введите Имя еще раз:")
        await state.set_state(Questionnaire.question2)


@router.message(Questionnaire.question3)
async def process_set_id_user(message: Message, state: FSMContext):
    try:
        Questionnaire.user.update("id", int(message.text))
        user = Questionnaire.user.get_info()
        msg = f"""Зарегестрирован:
        Фамилия: {user['surname']}
        Имя: {user['name']}
        id: {user['id']}
        """
        await message.answer(msg, reply_markup=get_create_user())
        await state.set_state(Questionnaire.question4)
    except:
        await message.answer("Ошибка ввода.\n Введите id еще раз:")
        await state.set_state(Questionnaire.question3)


@router.callback_query(F.data == "serch_user")
async def add_new_user(callback: types.CallbackQuery, state: FSMContext):
    msg = f"""
    Поиск участника
    Введите id учатника:    
    """
    await callback.message.answer(msg)
    await state.set_state(SearchUser.question1)


@router.message(SearchUser.question1)
async def process_set_name_user(message: Message, state: FSMContext):
    id_user = message.text
    msg = f"""Поиск id: {id_user}"""
    await message.answer(msg)
    await state.clear()


@router.callback_query(F.data == "enter_new_uesr" or F.data == "back_to_menu", Questionnaire.question4)
async def add_new_user(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "enter_new_uesr":
        user = Questionnaire.user.get_info()
        list_user.append(copy.deepcopy(Questionnaire.user))
        msg = f"""
Участник добавлен!
Фамилия: {user['surname']}
Имя: {user['name']}
id: {user['id']}
"""
        await callback.message.edit_text(msg, reply_markup=get_add_category_data(Questionnaire.user.events))
    if callback.data == "back_to_menu":
        msg = f"""
        Операция добавления отменена!
        Фамилия: {user['surname']} Имя: {user['name']} id: {user['id']}
        """
        await callback.message.edit_text(msg, reply_markup=get_main_menu_kb())
    await state.clear()


@router.callback_query(F.data.startswith("category_"))
async def add_new_user(callback: types.CallbackQuery):

    if callback.data == "category_1":
        await callback.message.edit_text(text=f"Категория {}")
