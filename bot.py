import telebot
from telebot import types

bot = telebot.TeleBot("1710349751:AAEbrPWG87ajN3UMRl6an0g4s2LvwzlP2PY")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['download'])
def welcome(message):
    sent_msg = bot.send_message(message.chat.id, "Welcome to bot. Which book do you want to download ?")
    bot.register_next_step_handler(sent_msg, searched_book_handler)


def searched_book_handler(message):
    searched_book = message.text

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    books = ['title 1. Author 1', 'title 2. Author 2', 'title 2. Author 2', 'title 3. Author 3']
    markup.add(*[types.KeyboardButton(book) for book in books])

    sent_msg = bot.send_message(
        message.chat.id,
        f"fdfddfdfdfddfddfdfdf",
        reply_markup=markup
    )
    bot.register_next_step_handler(sent_msg, book_detail_handler)


def book_detail_handler(message):
    selected_book = message.text
    bot.send_message(message.chat.id, f'you choose {selected_book}')

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    books = ['fb2', 'epub', 'mobi']
    markup.add(*[types.KeyboardButton(book) for book in books])

    sent_msg = bot.send_message(message.chat.id, f'Select book format', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, book_formats_handler)


def book_formats_handler(message):
    book_format = message.text

    bot.send_message(message.chat.id, f'you choose {book_format}')

    book_url = f'https://flibusta.site/b/485994/{book_format}'
    bot.send_message(message.chat.id, f'Click link to download book: {book_url}')


bot.polling()
