from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_sprite():
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="Sprite 1,5L"), KeyboardButton(text="Sprite 1L"))
    kb.add(KeyboardButton(text="Sprite 0,5L"))
    kb.adjust(2,1 )
    return kb.as_markup(reply_markup=True)
