import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Включение логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Массив с шутками
JOKES = [
    "Зачем классам нужны домашние задания? Чтобы они не скучали без меня!",
    "Почему программист не может поспать? Потому что у него всегда стоит задача!",
    "Как называют программиста, который не любит документацию? Безумцем.",
    "Зачем веб-разработчику часы? Чтобы отслеживать, сколько времени он тратит на баги!",
    "Почему базу данных называют «умной»? Потому что она запоминает всё, даже то, что вы забыли!",
    "Что делает программист на природе? Дерево обходит, чтобы не встретиться с багом!",
    "Зачем коту компьютер? Чтобы искать «все шарики» в интернете!",
    "Как научить робота танцевать? Просто дай ему пару библиотек и буфер обмена!",
    "Почему разработчик ненавидит солнечные лучи? Они всегда мешают видеть код!",
    "Что кричит программист, когда теряет данные? «О нет, опять глюки в бэкапе!»"
]

async def random_joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка рандомной шутки."""
    joke = random.choice(JOKES)
    await update.message.reply_text(joke)

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token("8389980079:AAFCXlJ2GtYoYdFIcoHdvK239uVRKsZ0k9c").build()

    # Регистрация команды /random
    application.add_handler(CommandHandler("random", random_joke))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()