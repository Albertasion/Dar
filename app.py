from loader import dp, bot
from utils.db_api.database import create_db
from handlers import register_handlers_start, register_handlers_profile_reg


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await create_db()
    await on_startup_notify(dp)


async  def on_shutdown(dp):
    await bot.close()

if __name__ == '__main__':
    from aiogram import executor
    register_handlers_start(dp)
    register_handlers_profile_reg(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
