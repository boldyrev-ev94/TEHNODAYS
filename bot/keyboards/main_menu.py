from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types
from model.User import User
from model.Category import Category


def get_main_menu_kb() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    btn1 = types.InlineKeyboardButton(
        text="Добавить участника", callback_data="add_new_user")
    btn2 = types.InlineKeyboardButton(
        text="Найти участника", callback_data="serch_user")
    builder.add(btn1)
    builder.row(btn2)
    return builder.as_markup()  # type: ignore


def get_create_user() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    btn_enter = types.InlineKeyboardButton(
        text="Отправить", callback_data="enter_new_uesr")
    btn_back = types.InlineKeyboardButton(
        text="Отменить", callback_data="back_to_menu")
    builder.add(btn_back, btn_enter)
    return builder.as_markup()  # type: ignore


def get_add_category_data(events) -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    list_btn = []
    for i, event in enumerate(events):
        list_btn.append(types.InlineKeyboardButton(
            text=f"Категория {event.get_name()}", callback_data=f"category_{i+1}"))
    builder.add(list_btn[0])
    for id_btn in range(1, len(list_btn)):
        builder.row(list_btn[id_btn])

    return builder.as_markup()
