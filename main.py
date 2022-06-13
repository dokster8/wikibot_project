import telebot
from telebot import types
from settings import token
import wikipedia
from logger import logger

wikipedia.set_lang("ru")
bot = telebot.TeleBot(token)
print('Server on-line')


@bot.message_handler(commands=['help', 'start'])
def help_command(message):
    bot.send_message(message.from_user.id,
                     'Добро пожаловать в Википедию. Введите интересующее вас слово.')


@bot.message_handler()
def summary_comand(message):
    word = message.text
    title = wikipedia.page(word).title
    page = wikipedia.page(word).url
    summary = wikipedia.summary(word)
    logger(message, word)
    bot.send_message(message.from_user.id, f'{title}\n{summary}\n{page}')


bot.infinity_polling()

print('Server off-line')
