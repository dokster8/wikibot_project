import datetime
import telebot
from settings import token
bot = telebot.TeleBot(token)


def logger(message, some_data):
    spy_data = [f'Пользователь: {message.from_user.full_name}', f' ID: {message.from_user.id}',
                f' Время запроса: {datetime.datetime.now()}', f' Запрос: "{some_data}"']
    f = open('wiki_logger.csv', 'a')
    f.write(','.join(spy_data))
    f.close
