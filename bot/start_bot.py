import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import main_menu
from aiogram.fsm.storage.memory import MemoryStorage
storage = MemoryStorage()


# Запуск бота
async def main():
    bot = Bot(token=config.bot_token.get_secret_value())

    dp = Dispatcher(storage=storage)
    dp.include_routers(main_menu.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
