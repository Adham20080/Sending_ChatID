import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart
from db import Database
from root import TOKEN, ADMIN_ID
from buttons import keyboard

db = Database("users.db")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    db.add_user(message.from_user.id, message.from_user.full_name)
    if message.from_user.id == ADMIN_ID:
        await message.answer("Hello", reply_markup=keyboard)
    else:
        await message.answer("Hello")


@dp.message(F.text == "Chat users")
async def chat_users(message: Message, bot: Bot):
    for user in db.all_userid():
        await bot.send_message(chat_id=user[0], text="Hello User!")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
