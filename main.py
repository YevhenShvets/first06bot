import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import MainMenu
import db

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Привіт✋✋✋\nЯ тестовий телеграм бот\nНажимай на кнопки", reply_markup=MainMenu.r_markup)

@dp.message_handler(commands=['about'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Це мій перший телеграм бот\nНе суди строго 🙏🙏🙏\nCreate by _Shvets Yevhen_", parse_mode="Markdown")


@dp.message_handler(content_types=['text'])
async def mm(message: types.Message):
    if message.text == "Товари📦":
        for t in db.data:
            await bot.send_message(message.from_user.id, db.output(t), parse_mode="Markdown")
    elif message.text == "Категорії🔡":
        for c in db.get_categories():
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Вибрати👆", callback_data=c[0])
            keyboard.add(callback_button)
            await bot.send_message(message.chat.id, "*{c}*".format(c=str(c[1])), reply_markup=keyboard, parse_mode="Markdown")


@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.id:
        for id, name in db.get_categories():
            if callback_query.data == str(id):
                await bot.send_message(callback_query.message.chat.id, f"`Категорія:` *{callback_query.message.text}*\n`Товари:`", parse_mode="Markdown")
                for t in db.get_tovar(id):
                    await bot.send_message(callback_query.message.chat.id, db.output(t), parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)